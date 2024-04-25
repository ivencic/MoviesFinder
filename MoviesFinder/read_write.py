import mysql.connector
from const import dbconfig_w


class DatabaseHandler:
    def __init__(self, name):
        self.name = name
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**dbconfig_w)
            print("Соединение с базой установлено.")
        except mysql.connector.Error as err:
            print(f"Eroare la conectare la bază de date: {err}")

    def create_top_search_table(self):
        if self.connection is None:
            print("Nu s-a stabilit nicio conexiune la baza de date.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS top_search (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    param VARCHAR(255),
                    query TEXT
                )
            """)
            print("Table 'top_search' is create or exist.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error to create table 'top_search': {err}")

    def insert_into_top_search(self, param, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""INSERT INTO top_search (param, query) VALUES (%s, %s)""", (param, query))
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Eroare la inserarea valorilor în tabela 'top_search': {err}")

    def execute_max_param_query(self):
        try:
            if self.connection is None:
                print("Conexiunea la baza de date nu a fost stabilită.")
                return None

            cursor = self.connection.cursor()
            cursor.execute("SELECT query FROM top_search WHERE param = (SELECT MAX(param) FROM top_search);")
            max_param = cursor.fetchone()[0]
            print(max_param)
            return max_param
        except mysql.connector.Error as err:
            print(f"Eroare la executarea query-ului: {err}")
            return None


db_handler = DatabaseHandler("top_search")
db_handler.connect()
db_handler.create_top_search_table()
db_handler.insert_into_top_search("genre", "SELECT * FROM movies WHERE genre = 'Comedy'")
max_param = db_handler.execute_max_param_query()


