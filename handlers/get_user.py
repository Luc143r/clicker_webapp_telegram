from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

import json
from json import JSONDecodeError

from datetime import datetime
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))

from data import db


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_id = ""
username = ""


@app.post("/get-data")
async def get_user(request: Request):
    global user_id
    global username
    
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        print('No Content-Type provided')
        raise HTTPException(status_code=400, detail='No Content-Type provided')
    elif content_type == 'application/json':
        try:
            result = await request.json()
            user_id = result['user_id']
            username = result['username']
            print(f'\n{datetime.now()}\n/get-data\nUser ID: {user_id}; Username: {username}')
            db.add_user(result['user_id'], result['username'])
            db.add_boost(result['user_id'], "power_click", 1)
            return JSONResponse(status_code=200, content=result)
        except JSONDecodeError:
            print('Invalid JSON data')
            raise HTTPException(status_code=400, detail='Invalid JSON data')
    else:
        print('Content-Type not supported')
        raise HTTPException(status_code=400, detail='Content-Type not supported')


@app.get("/get-user")
async def get_user_id():
    global user_id
    global username
    user_data = {'user_id': user_id, 'username': username}
    user_id = ''
    username = ''
    print(f'\n{datetime.now()}\n/get-user\nUser ID: {user_id}; Username: {username}')
    return JSONResponse(content=user_data, media_type="application/json")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)