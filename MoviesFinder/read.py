import mysql.connector
from const import dbconfig


class ReadDB:
    def __init__(self):
        self.connection = None
        self.conn = None
        self.get_connection()

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(**dbconfig)
        except mysql.connector.Error as e:
            print(f"Ошибка соединения: {e}. Работа программы завершена.")
            exit()

    def execute_query_read(self, query):
        result = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        except mysql.connector.Error as e:
            print(f'Ошибка: \'{e}\' в запросе: {query}')
        finally:
            cursor.close()
        return result



