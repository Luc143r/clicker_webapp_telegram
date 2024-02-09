import flet as ft


class BoostsView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super(BoostsView, self).__init__(
            route='/boost', horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )

        self.page = page
        self.navbar = navbar
        self.content_boost = ft.Container(
            ft.Column(controls=[
                ft.Container(content=ft.Row(
                    controls=[
                        ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Column([ft.Icon(name=ft.icons.FLASH_ON)], horizontal_alignment=ft.CrossAxisAlignment.START),
                                ft.Column([ft.Row([ft.Text('PowerClick')]), ft.Row([ft.Text('LVL: 0')])],
                                          horizontal_alignment=ft.CrossAxisAlignment.START),
                            ], spacing=50),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column([
                            ft.Row(controls=[ft.Text('COST')]),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ), border=ft.Border(bottom=ft.BorderSide(3, 'black')), border_radius=ft.BorderRadius(20, 20, 20, 20), padding=ft.Padding(30, 10, 30, 10)),
                ft.Container(content=ft.Row(
                    controls=[
                        ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Column([ft.Icon(name=ft.icons.ADS_CLICK)],
                                          horizontal_alignment=ft.CrossAxisAlignment.START),
                                ft.Column([ft.Row([ft.Text('Boost 2')]), ft.Row([ft.Text('LVL: 0')])],
                                          horizontal_alignment=ft.CrossAxisAlignment.START),
                            ], spacing=50),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column([
                            ft.Row(controls=[ft.Text('COST')]),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ), border=ft.Border(bottom=ft.BorderSide(3, 'black')), border_radius=ft.BorderRadius(20, 20, 20, 20), padding=ft.Padding(30, 10, 30, 10))
            ], spacing=20),
            height=self.page.height * 0.3,
            width=self.page.width * 0.8,
        )

        self.controls = [
            ft.Text('Boosts', size=30, color='#ff8b1f'),
            self.content_boost,
            self.navbar
        ]
