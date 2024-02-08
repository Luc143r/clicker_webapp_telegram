import flet as ft
from data import db


class LeaderboardView(ft.View):
    def __init__(self, page: ft.Page, navbar: ft.NavigationBar):
        super().__init__(
            route="/leaderboard", horizontal_alignment='center', vertical_alignment='center', bgcolor='#141221'
        )

        self.page = page
        self.navbar = navbar
        self.leaderboard = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Пользователь")),
                ft.DataColumn(ft.Text("Счет"))
            ],
            rows=[],
        )
        rows = self.get_leaderboard_rows()
        for row in rows:
            self.leaderboard.rows.insert(len(rows), row)

        self.controls = [
            self.leaderboard,
            self.navbar
        ]

    def get_leaderboard_rows(self):
        table = []
        users = db.get_all_users()[:10]
        for user in users:
            table.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.TextButton(text=f"@{user['username']}", url=f"https://t.me/{user['username']}")),
                    ft.DataCell(ft.Text(str(user['point'])))
                ]
            ))
        return table
