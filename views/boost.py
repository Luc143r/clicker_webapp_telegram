import flet as ft
from configs.config_reader import Config


class BoostsView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super(BoostsView, self).__init__(
            route='/boost', horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )
        
        self.page = page
        self.navbar = navbar
        self.content_boost = ft.Text('Хуев тебе под сраку. Пивка для рывка и погнал!')
        
        self.controls = [
            self.content_boost,
            self.navbar
        ]
