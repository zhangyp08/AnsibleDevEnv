import configparser

config = configparser.ConfigParser()
config.read('config/dbconfig.conf')

db = 'TESTDB'
host = config[db]['host']
port = config[db]['port']
user = config[db]['user']
passwd = config[db]['passwd']
db_name = config[db]['db']
charset = config[db]['charset']

print(host)
print(charset)