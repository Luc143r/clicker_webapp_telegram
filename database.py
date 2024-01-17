import pymysql


class Database:
    def __init__(self):
        self.host = '127.0.0.1',
        self.port = 8000,
        self.user = 'root',
        self.password='root',
        self.database='points',
        self.cursor=pymysql.cursors.DictCursor
        