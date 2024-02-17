import flet as ft

from views import BoobsView, LeaderboardView, BoostsView
from data import db

import aiohttp
import asyncio

import requests
from fastapi import HTTPException
from configs.config_reader import Config


# Дорогой разработчик:
# Когда я писал этот код, только бог и я
# знали, как он работает.
# Теперь знает только бог!

# Но. Если ты пытаешься что-то оптимизировать
# в моем коде и у тебя не получается,
# пожалуйста, увеличь значение счётчика
# как предупреждение для следующего человека:
    
# Часов_потрачено_здесь = 161


async def main(page: ft.Page):
    #Page settings
    page.title = 'BoobsCoin'
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {'JetBrainsMono': 'fonts/JetBrainsMono.ttf'}
    page.theme = ft.Theme(font_family='JetBrainsMono')
    
    
    async def click_navbar(event: ft.TapEvent) -> None:
        #Boobs page on navbar
        if int(event.data) == 0:
            await page.go_async("/boobs")
        #Leaderboard page on navbar
        elif int(event.data) == 1:
            await page.go_async("/leaderboard")
        #Boost page on navbar
        elif int(event.data) == 2:
            await page.go_async("/boost")
        else:
            await page.go_async("/boobs")

        await page.update_async()
        
    
    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, 
                                    selected_icon=ft.icons.HOME_ROUNDED, 
                                    label='Boobs'),
            ft.NavigationDestination(icon=ft.icons.LEADERBOARD_OUTLINED, 
                                    selected_icon=ft.icons.LEADERBOARD, 
                                    label='Leaderboard'),
            ft.NavigationDestination(icon=ft.icons.ROCKET_LAUNCH_OUTLINED, 
                                    selected_icon=ft.icons.ROCKET_LAUNCH_ROUNDED, 
                                    label='Boost')
        ],
        adaptive=True,
        bgcolor='#141221',
        height=65,
        on_change=click_navbar
    )
    
    #Init views
    boobs_page = BoobsView(page, navbar)
    leaderboard_page = LeaderboardView(page, navbar)
    boost_page = BoostsView(page, navbar)
    

    async def fetch_user_data():
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{Config.get_config(0, "config_app").API_URL}/get-user', headers={'Content-Type': 'application/json'}) as response:
                try:
                    response = await response.json()
                    print(response)
                    user_id = response['user_id']
                    username = response['username']
                    return [user_id, username]
                except:
                    print('Invalid JSON data')
                    print(response)
                    raise HTTPException(status_code=400, detail='Invalid JSON data')
                finally:
                    await session.close()

    
    #Method routing
    async def router(route: str) -> None:
        page.views.clear()
        if page.route == "/":
            await page.go_async("/boobs")
            user_data = await fetch_user_data()
            if user_data[0]:
                user_point = db.get_point_user(user_data[0])
                page.session.set(str(page._session_id), user_data[0])
                power_click_lvl = db.get_boost_lvl(str(page.session.get(str(page._session_id))), 'power_click')
                page.session.set('power_click', power_click_lvl)
                
                boobs_page.score.data = int(user_point)
                boobs_page.score.value = str(user_point)
                boobs_page.power_click = int(page.session.get('power_click'))
                page.session.set(str(page.session.get(str(page._session_id))), boobs_page.score.value)
        elif page.route == "/boobs":
            if page.session.get('power_click'):
                boobs_page.power_click = int(page.session.get('power_click'))
            page.views.append(boobs_page)
        elif page.route == "/leaderboard":
            page.views.append(leaderboard_page)
        elif page.route == '/boost':
            if page.session.get('power_click'):
                boost_page.power_click_lvl.data = int(page.session.get('power_click'))
                boost_page.power_click_lvl.value = f'LVL: {str(page.session.get("power_click"))}'
                if page.session.get('power_click') != 0:
                    index_price = float(Config.get_config(1, 'config_boosts').PRICE_STEP) ** int(page.session.get('power_click'))
                    final_price = int(Config.get_config(1, 'config_boosts').START_PRICE * index_price)
                    boost_page.power_click_cost.data = int(final_price)
                    boost_page.power_click_cost.value = str(final_price)
            page.views.append(boost_page)
        else:
            page.views.append(boobs_page)
        
        await page.update_async()
        
    async def close_session(event) -> None:
        if page.session.get_keys():
            if page.session.get(str(page._session_id)) != '':
                try:
                    user_point = db.get_point_user(page.session.get(str(page._session_id)))
                    user_session_point = page.session.get(str(page.session.get(str(page._session_id))))
                    if user_session_point > user_point:
                        db.update_user_point(page.session.get(str(page._session_id)), int(user_session_point))
                    #db.update_user_point(page.session.get(str(page._session_id)), int(user_point) + int(page.session.get(str(page.session.get(str(page._session_id))))))
                except:
                    print(f'User point: {user_point}\nSession point: {page.session.get(str(page.session.get(str(page._session_id))))}')
            #page.session.remove(str(page._session_id))
            print(f'User_sessions dict: {page.session.get_keys()}\nPage closed')
    
    page.on_route_change = router
    page.on_disconnect = close_session
    await page.go_async("/")


if __name__ == '__main__':
    try:
        text = 'App started'
        print(f'{text:*^30}')
        ft.app(target=main, view=None, port=8000)
    except:
        text = 'App not started'
        print(f'{text:*^30}')
