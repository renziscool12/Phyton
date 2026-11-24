import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="std_db",
        cursorclass=pymysql.cursors.DictCursor
    )
