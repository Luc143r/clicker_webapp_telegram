import flet as ft
import asyncio


class Mainpage:
    def __init__(self, width):
        self.width = width
        self.score = ft.Text(value='0', size=60, data=0)
        self.score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
        self.image = ft.Image(src='boobs.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
        self.progress_bar = ft.ProgressBar(value=0, width=self.width-60, bar_height=20, color='#ff8b1f', bgcolor='#bf6524')
        self.navbar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, 
                                        selected_icon=ft.icons.HOME_ROUNDED, 
                                        label='Boobs'),
                ft.NavigationDestination(icon=ft.icons.LEADERBOARD_OUTLINED, 
                                        selected_icon=ft.icons.LEADERBOARD, 
                                        label='Leaderboard'),
                ft.NavigationDestination(icon=ft.icons.ROCKET_LAUNCH_OUTLINED, 
                                        selected_icon=ft.icons.ROCKET_LAUNCH_ROUNDED, 
                                        label='Boost'),
            ],
            adaptive=True,
            bgcolor='#141221',
            height=65,
            on_change=click_leaderbord
        )

        self.route = '/'
        self.controls = [
            self.score,
            ft.Container(
                content=ft.Stack(controls=[self.image, self.score_counter]),
                on_click=score_up,
                margin=ft.Margin(0, 0, 0, 50)
            ),
            ft.Container(
                content=self.progress_bar,
                border_radius=ft.BorderRadius(10, 10, 10, 10),
                margin=ft.Margin(0, 0, 0, 75)
            )
        ],
        self.navbar
        
        
'''x = Mainpage()
print(x.route)'''