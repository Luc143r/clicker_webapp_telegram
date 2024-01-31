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
            self.leaderboard.rows.insert(len(self.get_leaderboard_rows()), row)

        self.controls = [
            self.leaderboard,
            self.navbar
        ]

    def get_leaderboard_rows(self):
        class Users:
            def __init__(self, user_id, username, point):
                self.user_id = user_id
                self.username = username
                self.point = point

        users = []
        db_request = db.get_all_users()
        for user in db_request:
            users.append(Users(user['user_id'], user['username'], user['point']))

        table = []
        for user in users:
            table.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.TextButton(text=user.username)),
                    ft.DataCell(ft.Text(str(user.point)))
                ]
            ))
        return table
