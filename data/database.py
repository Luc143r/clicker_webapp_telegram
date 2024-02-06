import pymysql


def db_session(method):
    def wrapper(self, *args, **kwargs):
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            cursor = connection.cursor()
            connection.begin()
            try:
                result = method(self, *args, **kwargs, cursor=cursor)
                connection.commit()
                return result
            except Exception as e:
                print(f'Ошибка: {e}')
                connection.rollback()
                print('Откат изменений')
                cursor.execute("ALTER TABLE `boobscoin`.`users` AUTO_INCREMENT = 1")
                connection.commit()
            finally:
                cursor.close()
        except Exception as err:
            print(f'Произошла ошибка подключения: {err}')
        finally:
            if connection:
                connection.close()
    return wrapper


class Database:
    @db_session
    def __init__(self, cursor: pymysql.cursors.DictCursor):
        cursor.execute("CREATE DATABASE IF NOT EXISTS `boobscoin`")
        cursor.execute("USE `boobscoin`")
        cursor.execute("CREATE TABLE IF NOT EXISTS `users`(id int AUTO_INCREMENT," \
                        "user_id varchar(10) UNIQUE KEY," \
                        "username varchar(32)," \
                        "point int," \
                        "PRIMARY KEY(id))")
        
    @db_session
    def add_user(self, user_id: str, username: str, cursor: pymysql.cursors.DictCursor):
        cursor.execute("USE `boobscoin`")
        cursor.execute("INSERT INTO users (user_id, username, point) VALUES (%s, %s, %s)", (user_id, username, 0))
        
    @db_session
    def get_user(self, user_id: str, cursor: pymysql.cursors.DictCursor):
        cursor.execute("USE `boobscoin`")
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id))
        return cursor.fetchone()
    
    @db_session
    def get_point_user(self, user_id: str, cursor: pymysql.cursors.DictCursor):
        cursor.execute("USE `boobscoin`")
        cursor.execute("SELECT point FROM users WHERE user_id = %s", (user_id))
        return cursor.fetchone()['point']
    
    @db_session
    def get_all_users(self, cursor: pymysql.cursors.DictCursor):
        cursor.execute("USE `boobscoin`")
        cursor.execute("SELECT * FROM users ORDER BY point DESC")
        return cursor.fetchall()
        
    @db_session
    def update_user_point(self, user_id: str, point: int, cursor: pymysql.cursors.DictCursor):
        cursor.execute("USE `boobscoin`")
        cursor.execute("UPDATE users SET point = %s WHERE user_id = %s", (point, user_id))
