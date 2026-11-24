from Connection.conenction import get_connection

class StadentModel:

    def get_all_stadent(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM std_info")
                return cursor.fetchall()
        finally:
            connection.close()

    def get_stadent_by_id(self, student_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql ="SELECT * FROM std_info WHERE student_id = %s"
                cursor.execute(sql, (student_id,))
                return cursor.fetchone()
        finally:
            connection.close()

    def add_stadent(self, first_name, last_name, age, course):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO std_info(first_name, last_name, age, course) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (first_name, last_name, age, course))
                connection.commit()
                return cursor.lastrowid
        finally:
            connection.close()

    def update_stadent(self, first_name, last_name, age, course, student_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE std_info SET first_name = %s, last_name = %s, age = %s, course = %s WHERE student_id = %s"
                cursor.execute(sql, (first_name, last_name, age, course, student_id))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()

    def delete_stadent(self, student_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM std_info WHERE student_id = %s"
                cursor.execute(sql, (student_id,))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()

    def get_stadent_by_name(self, first_name, last_name):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM std_info WHERE first_name = %s AND last_name = %s"
                cursor.execute(sql, (first_name, last_name))
                return cursor.fetchone()
        finally:
            connection.close()
