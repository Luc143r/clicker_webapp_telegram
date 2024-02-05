import flet as ft

from views import BoobsView, LeaderboardView, BoostsView

import aiohttp
import asyncio
from fastapi import HTTPException


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
            async with session.get('https://52ds1b7g-8080.euw.devtunnels.ms/get-user', headers={'Content-Type': 'application/json'}) as response:
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
            user_data = await fetch_user_data()
            page.session.set(str(page._session_id), user_data[0])
            await page.go_async("/boobs")
        elif page.route == "/boobs":
            print(page.session.get(str(page._session_id)))
            page.views.append(boobs_page)
        elif page.route == "/leaderboard":
            page.views.append(leaderboard_page)
        elif page.route == '/boost':
            page.views.append(boost_page)
        else:
            page.views.append(boobs_page)
        
        await page.update_async()
        
    async def close_session(event) -> None:
        page.session.remove(str(page._session_id))
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
