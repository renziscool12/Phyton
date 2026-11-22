import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='ticket_db'
    )
    return connection
