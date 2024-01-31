from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Request, HTTPException
from pydantic import BaseModel
import json
from json import JSONDecodeError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get-data")
async def get_user(request: Request):
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        print('No Content-Type provided')
        raise HTTPException(status_code=400, detail='No Content-Type provided')
    elif content_type == 'application/json':
        try:
            result = await request.json()
            print(result)
            return await request.json()
        except JSONDecodeError:
            print('Invalid JSON data')
            raise HTTPException(status_code=400, detail='Invalid JSON data')
    else:
        print('Content-Type not supported')
        raise HTTPException(status_code=400, detail='Content-Type not supported')