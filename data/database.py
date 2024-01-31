import pymysql


def db_session(method):
    def wrapper(self, *args, **kwargs):
        connection = pymysql.connect(
            host='127.0.0.1',
            port=8000,
            user='root',
            password='admin',
            database='points',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()
        try:
            return method(self, *args, **kwargs, cursor=cursor)
        finally:
            connection.commit()
            connection.close()
    return wrapper


class Database:
    @db_session
    def __init__(self, cursor: pymysql.cursors.DictCursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS `point`(id int AUTO_INCREMENT," \
                        "user_id int," \
                        "username varcher(32)," \
                        "point int," \
                        "PRIMARY KEY(id))")
        
        