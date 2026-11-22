from TicketManagement.Database.connection import get_connection


class PersonModel:
    def __init__(self):
        self.connection = get_connection()


    def add_person(self, first_name, last_name):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO person(first_name, last_name) VALUES (%s, %s)"
                cursor.execute(sql, (first_name, last_name))
                connection.commit()
                return True
        except Exception as e:
            print(e)
            return False

    def get_person(self):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM person"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def update_person(self, person_id, first_name, last_name):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE person SET first_name = %s, last_name = %s WHERE person_id = %s"
                cursor.execute(sql, (first_name, last_name, person_id))
                connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            return False

    def delete_person(self, person_id):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM person WHERE person_id =%s"
                cursor.execute(sql, (person_id,))
                connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            return False
