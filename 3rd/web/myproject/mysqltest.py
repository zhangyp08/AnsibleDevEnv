import pymysql


host = "127.0.0.1"
user = "root"
password = "#1Danger0us"
db = "polls"

connection = pymysql.connect(host=host,
    user=user,
    password=password,
    db=db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor=connection.cursor()
real_sql = "select * from polls_question"
cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
cursor.execute(real_sql)
print(cursor.fetchall())
connection.close()