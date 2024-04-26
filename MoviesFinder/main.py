import read
import read_write
from tabulate import tabulate


def truncate_text(text, max_length=100):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


read = read.ReadDB()
db_handler = read_write.DatabaseHandler("top_search")
db_handler.connect()
db_handler.create_top_search_table()
max_param = db_handler.execute_max_param_query()

options = {
    "Top Searches": "SELECT * FROM movies",
    "Year": "SELECT * FROM movies WHERE year LIKE '%{}%'",
    "Genres": "SELECT * FROM movies WHERE genres LIKE '%{}%'",
    "Keyword": "SELECT * FROM movies WHERE plot LIKE '%{}%'"
}

print("1. Top Searches")
print("2. Year")
print("3. Genres")
print("4. Keyword")
option = input("Выберите опцию: ")

if option in options:
    limit = int(input("Введите лимит : ")) if option == "Top Searches" else None
    query_template = options[option]
    if "{}" in query_template:
        param = input(f"Input {option.lower()}: ")
        sql_query = query_template.format(param)
        result = read.execute_query_read(sql_query)
        db_handler.insert_into_top_search(option, sql_query)
        headers = ["id", "plot", "genres", "runtime", "cast", "poster", "title", "languages", "directors",
                   "awards.text", "year", "imdb.rating", "type"]
        result_truncated = [[truncate_text(cell) if idx in [1, 5] else cell for idx, cell in enumerate(row)] for row in
                            result]
        print(tabulate(result_truncated, headers=headers, tablefmt="grid"))
    else:
        sql_query = query_template
        result = read.execute_query_read(sql_query)
        headers = ["id", "plot", "genres", "runtime", "cast", "poster", "title", "languages", "directors",
                   "awards.text", "year", "imdb.rating", "type"]
        result_truncated = [[truncate_text(cell) if idx in [1, 5] else cell for idx, cell in enumerate(row)] for row in
                            result]
        print(tabulate(result_truncated, headers=headers, tablefmt="grid"))
else:
    print("Invalid option.")
