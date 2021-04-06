import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE hours (id int, hour text)"
cursor.execute(create_table)

hours = [(1, "10:30"), (2, "10:00"), (3, "11:30"), (4, "13:30"), (5, "15:30"), (6, "17:00"), (7, "18:30")]
insert_query = "INSERT INTO hours VALUES (?,?)"
cursor.executemany(insert_query, hours)

select_query = "SELECT * FROM hours"
for row in cursor.execute(select_query):
    print(row)



connection.commit()
connection.close()