import flet as ft
import asyncio


async def main(page: ft.Page):
    page.title = 'BoobsCoin'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'JetBrainsMono': 'fonts/JetBrainsMono.ttf'}
    page.theme = ft.Theme(font_family='JetBrainsMono')


    '''
    Event handler on click coin
    '''
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


    '''
    Event handler on click leaderboard
    '''
    async def click_navbar(event: ft.ContainerTapEvent) -> None:
        #Main page on navbar "Boobs"
        if int(event.data) == 0:
            await route_home(event)
        #Leaderboard page on navbar
        elif int(event.data) == 1:
            await route_leaderboard(event)
        #Boost page on navbar
        elif int(event.data) == 2:
            await route_boost(event)
        else:
            await route_home(event)
        await page.update_async()


    '''
    Main page layout
    '''
    score = ft.Text(value='0', size=60, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
    image = ft.Image(src='boobs.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    progress_bar = ft.ProgressBar(value=0, width=page.width-60, bar_height=20, color='#ff8b1f', bgcolor='#bf6524')
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
        on_change=click_navbar
    )


    '''
    Leaderboard layout example
    '''
    top_one_user = ft.ListTile(
        leading=ft.Icon(ft.icons.ONETWOTHREE),
        title=ft.Text('@insearchofmyself666 топ 1, кто же еще')
    )
    top_two_user = ft.ListTile(
        leading=ft.Icon(ft.icons.ONETWOTHREE),
        title=ft.Text('@qzlegenda топ 2, так и быть')
    )


    async def route_home(event: ft.TapEvent) -> None:
        await page.go_async('/')

    async def route_leaderboard(event: ft.TapEvent) -> None:
        await page.go_async('/leaderboard')

    async def route_boost(event: ft.TapEvent) -> None:
        await page.go_async('/boost')


    async def route_change(route):
        page.views.clear()
        if page.route == '/':
            page.views.append(
            ft.View(
                '/',
                [
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
                    navbar,
                ],
                #avigation_bar=navbar,
                vertical_alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                bgcolor='#141221'
            )
        )
        if page.route == '/leaderboard':
            page.views.append(
            ft.View(
                '/leaderboard',
                [
                    top_one_user,
                    top_two_user,
                    navbar,
                ],
                #navigation_bar=navbar,
                vertical_alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                bgcolor='#141221'
            )
        )
        if page.route == '/boost':
            page.views.append(
            ft.View(
                '/boost',
                [
                    ft.Text('Хуев тебе под сраку. Пивка для рывка и погнал!'),
                    navbar,
                ],
                #navigation_bar=navbar,
                vertical_alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                bgcolor='#141221'
            )
        )
        await page.update_async()

    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        await page.go_async(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    await page.go_async(page.route)


if __name__ == '__main__':
    try:
        text = 'App started'
        print(f'{text:*^30}')
        ft.app(target=main, view=None, port=8000)
    except:
        text = 'App not started'
        print(f'{text:*^30}')