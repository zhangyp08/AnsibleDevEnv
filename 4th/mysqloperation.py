import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig

config = configparser.ConfigParser()
config.read(GetTestConfig('dbconfig.conf'))

db = 'TESTDB'
host = config[db]['host']
port = config[db]['port']
user = config[db]['user']
passwd = config[db]['passwd']
db_name = config[db]['db']
charset = config[db]['charset']

# host = "127.0.0.1"
# user = "root"
# password = "#1Danger0us"
# db = "polls"

class MySQLcaozuo():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"

        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def search(self, table_name):
        real_sql = "select * from {}".format(table_name)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def update(self, table_name, data):
        real_sql = "update {} SET ".format(table_name, data)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()


    def close(self):
        self.connection.close()


if __name__=='__main__':
    db = MySQLcaozuo()
    table_name="polls_question"
    data = {'id':1, 'question_text': 'what is your favorite game?', 'pub_date': '2018-11-16 15:52:05.000000'}
    db.clear(table_name)
    db.insert(table_name,data)
    db.close()
