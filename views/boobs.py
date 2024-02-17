import flet as ft
import asyncio
from data import db


class BoobsView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super(BoobsView, self).__init__(
            route="/", horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )
        
        self.page = page
        self.score = ft.Text(value='0', size=60, data=0)
        self.score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
        self.image = ft.Image(src='coin.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
        self.progress_bar = ft.ProgressBar(value=0, width=self.page.width-60, bar_height=20, color='#ff8b1f', bgcolor='#bf6524')
        self.navbar = navbar
        
        self.power_click = 1


        self.controls = [
            self.score,
            ft.Container(
                content=ft.Stack(controls=[self.image, self.score_counter]),
                on_click=self.score_up,
                margin=ft.Margin(0, 0, 0, 50)
            ),
            ft.Container(
                content=self.progress_bar,
                border_radius=ft.BorderRadius(10, 10, 10, 10),
                margin=ft.Margin(0, 0, 0, 75)
            ),
            self.navbar
        ]
    
    async def score_up(self, event: ft.ContainerTapEvent) -> None:
        self.score.data += self.power_click
        self.score.value = str(self.score.data)
        
        self.page.session.set(str(self.page.session.get(str(self.page._session_id))), self.score.data)
        
        self.image.scale = 0.95
        self.score_counter.opacity = 50
        self.score_counter.value = f'+{self.power_click}'
        self.score_counter.right = 0
        self.score_counter.left = event.local_x
        self.score_counter.top = event.local_y
        self.score_counter.bottom = 0
        self.progress_bar.value += (1 / 100)

        
        if self.score.data % 100 == 0:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='100 раз кликнул по монете',
                    size=25,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            self.page.snack_bar.open = True
            self.progress_bar.value = 0
        
        if self.score.data == 300:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='300 раз! Секс-гигант',
                    size=25,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            self.page.snack_bar.open = True
            self.progress_bar.value = 0
        

        await self.page.update_async()
        
        self.image.scale = 1
        self.score_counter.opacity = 0
        await self.page.update_async()