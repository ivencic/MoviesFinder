import mysql.connector
import read
import read_write
import querys

read = read.ReadDB()

db_handler = read_write.DatabaseHandler("top_search")
db_handler.connect()
db_handler.create_top_search_table()
db_handler.insert_into_top_search("genre", "SELECT * FROM movies WHERE genre = 'Comedy'")
max_param = db_handler.execute_max_param_query()


print("1. Top Searches")
print("2. Year")
print("3. Genres")
print("4. Keyword")
option = input("Выберите опцию (соотвествующую цифру): ")
result = []
if option == "1":
    limit = int(input("Введите лимит : "))
    sql_query = f"SELECT * FROM movies"
    result = read.execute_query_read(sql_query)
    print(*result)


elif option == "2":
    year = input("Input year find year: ")
    #limit = input("Введите лимит : ")
    sql_query = f"SELECT * FROM movies WHERE year LIKE '{year}';"
    result = read.execute_query_read(sql_query)
    print(result)

elif option == "3":
    gen = input("Input genres: ")
    #limit = input("Введите лимит : ")
    sql_query = f"SELECT * FROM movies WHERE genres LIKE '{gen}';"
    result = read.execute_query_read(sql_query)
    print(result)

elif option == "4":
    key = input("Input keyword: ")
    # limit = input("Введите лимит : ")
    sql_query = f"SELECT * FROM movies WHERE plot LIKE '%{key}%';"
    result = read.execute_query_read(sql_query)
    print(result)

else:
    print("Invalid option.")
