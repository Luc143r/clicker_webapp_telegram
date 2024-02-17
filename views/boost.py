import flet as ft

from data import db
from configs.config_reader import Config


class BoostsView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super(BoostsView, self).__init__(
            route='/boost', horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )

        self.page = page
        self.navbar = navbar
        self.power_click_lvl = ft.Text(value='LVL: 0', data=0)
        self.power_click_cost = ft.Text(value='10000', data=10000)
        
        self.content_boost = ft.Container(
            ft.Column(controls=[
                ft.Container(content=ft.Row(
                    controls=[
                        ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Column([ft.Icon(name=ft.icons.FLASH_ON)], horizontal_alignment=ft.CrossAxisAlignment.START),
                                ft.Column([ft.Row([ft.Text('PowerClick')]), self.power_click_lvl],
                                          horizontal_alignment=ft.CrossAxisAlignment.START),
                            ], spacing=50),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column([
                            ft.Row(controls=[self.power_click_cost]),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ), border=ft.Border(bottom=ft.BorderSide(3, 'black')), border_radius=ft.BorderRadius(20, 20, 20, 20), padding=ft.Padding(30, 10, 30, 10), on_click=self.buy_power_click),
                ft.Container(content=ft.Row(
                    controls=[
                        ft.Column(controls=[
                            ft.Row(controls=[
                                ft.Column([ft.Icon(name=ft.icons.ADS_CLICK)],
                                          horizontal_alignment=ft.CrossAxisAlignment.START),
                                ft.Column([ft.Row([ft.Text('В разработке')]), ft.Row([ft.Text('LVL: 0')])],
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
    
    async def buy_power_click(self, event: ft.ContainerTapEvent):
        currency = self.page.session.get(str(self.page.session.get(str(self.page._session_id))))
        if int(currency) >= self.power_click_cost.data:
            self.page.session.set(str(self.page.session.get(str(self.page._session_id))), currency - self.power_click_cost.data)
            db.update_user_point(self.page.session.get(str(self.page._session_id)), currency - self.power_click_cost.data)
            self.page.session.set('power_click', int(self.page.session.get('power_click')) + 1)
            db.update_boost(self.page.session.get(str(self.page._session_id)), 'power_click', self.page.session.get('power_click'))
            self.power_click_lvl.data = int(self.page.session.get('power_click'))
            self.power_click_lvl.value = f'LVL: {str(self.page.session.get("power_click"))}'
            index_price = float(Config.get_config(1, 'config_boosts').PRICE_STEP) ** int(self.page.session.get('power_click'))
            final_price = int(Config.get_config(1, 'config_boosts').START_PRICE * index_price)
            self.power_click_cost.data = int(final_price)
            self.power_click_cost.value = str(final_price)
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='PowerClick улучшен :)',
                    size=15,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            self.page.snack_bar.open = True
        else:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='Не хватает монет :(',
                    size=15,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )
            self.page.snack_bar.open = True
        await self.page.update_async()
