import flet as ft


class LeaderboardView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super().__init__(
            route="/leaderboard", horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )
        
        self.page = page
        self.navbar = navbar
        self.top_one = ft.ListTile(
            leading=ft.Icon(ft.icons.ONETWOTHREE),
            title=ft.Text("@insearchofmyself666 топ 1, кто же еще")
        )
        self.top_two = ft.ListTile(
            leading=ft.Icon(ft.icons.ONETWOTHREE),
            title=ft.Text('@qzlegenda топ 2, так и быть')
        )
        
        self.controls = [
            self.top_one,
            self.top_two,
            self.navbar
        ]
        