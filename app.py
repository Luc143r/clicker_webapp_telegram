import asyncio
import flet as ft


async def main(page: ft.Page) -> None:
    page.title = 'BoobsCoin'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'JetBrainsMono': 'fonts/JetBrainsMono.ttf'}
    page.theme = ft.Theme(font_family='JetBrainsMono')

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)
        
        image.scale = 0.95
        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = event.local_x
        score_counter.top = event.local_y
        score_counter.bottom = 0
        progress_bar.value += (1 / 100)

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='100 раз кликнул по монете',
                    size=25,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            page.snack_bar.open = True
            progress_bar.value = 0

        if score.data == 300:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='300 раз! Секс-гигант',
                    size=25,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            page.snack_bar.open = True
            progress_bar.value = 0
        await page.update_async()
        
        await asyncio.sleep(0.1)
        
        image.scale = 1
        score_counter.opacity = 0
        await page.update_async()


    async def click_leaderbord(event: ft.ContainerTapEvent) -> None:
        score.value = 0
        text = ''
        if int(event.data) == 0:
            await page.clean_async()
            await page.add_async(
                score,
                ft.Container(
                    content=ft.Stack(controls=[image, score_counter]),
                    on_click=score_up,
                    margin=ft.Margin(0, 0, 0, 50)
                ),
                ft.Container(
                    content=progress_bar,
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    margin=ft.Margin(0, 0, 0, 75)
                ),
                navbar
            )
            text = 'Boobs page'
        elif int(event.data) == 1:
            await page.clean_async()
            temporary_text = ft.Text('Раздел Leaderboard в разработке')
            await page.add_async(temporary_text, navbar)
            text = 'Leaderboard page'
        elif int(event.data) == 2:
            await page.clean_async()
            temporary_text = ft.Text('Раздел Boost в разработке')
            await page.add_async(temporary_text, navbar)
            text = 'Boost page'
        else:
            await page.clean_async()
            temporary_text = ft.Text('Что-то пошло не так')
            await page.add_async(temporary_text, navbar)
            text = 'Чет хуйня какая-то'
        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                value=text,
                size=25,
                color='#ff8b1f',
                text_align=ft.TextAlign.CENTER
            ),
            bgcolor='#25223a'
        )
        page.snack_bar.open = True
        await page.update_async()


    score = ft.Text(value='0', size=60, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
    image = ft.Image(src='coin.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    progress_bar = ft.ProgressBar(value=0, width=page.width-60, bar_height=15, color='#ff8b1f', bgcolor='#bf6524')
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
                                    label='Boost'),
        ],
        adaptive=True,
        bgcolor='#141221',
        height=65,
        on_change=click_leaderbord
    )
    
    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 50)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10),
            margin=ft.Margin(0, 0, 0, 75)
        ),
        navbar
    )


if __name__ == '__main__':
    ft.app(target=main, view=None, port=8000)