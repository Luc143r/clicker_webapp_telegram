import flet as ft

from views import BoobsView, LeaderboardView, BoostsView
from handlers import get_user

from aiohttp.web_request import Request
import requests
import asyncio


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
    
    #Method routing
    async def router(route: str) -> None:
        page.views.clear()
        if page.route == "/":
            await page.go_async("/boobs")
        elif page.route == "/boobs":
            page.views.append(boobs_page)
        elif page.route == "/leaderboard":
            page.views.append(leaderboard_page)
        elif page.route == '/boost':
            page.views.append(boost_page)
        else:
            page.views.append(boobs_page)
        
        await page.update_async()


    page.on_route_change = router
    await page.go_async("/")


if __name__ == '__main__':
    try:
        text = 'App started'
        print(f'{text:*^30}')
        ft.app(target=main, view=None, port=8000)
    except:
        text = 'App not started'
        print(f'{text:*^30}')
