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
option = input("Alege opțiunea: ")

if option == "1":
    limit = int(input("Introduceți limita de afișare: "))
    sql_query = f"{max_param} LIMIT {limit}"
    result = read.execute_query_read(sql_query)
    for i in len(result):
        print(result)


elif option == "2":

    pass
elif option == "3":

    pass
elif option == "4":

    pass
else:
    print("Opțiune invalidă.")




