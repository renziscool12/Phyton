from TicketManagement.Database.connection import get_connection

class TicketModel:
    def __init__(self):
        self.connection = get_connection()

    def add_ticket(self, event_name, registration_date):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql ="INSERT INTO ticket (event_name, registration_date) VALUES (%s, %s"
                cursor.execute(sql, (event_name, registration_date))
                connection.commit()
                return True
        except Exception as e:
            print(e)
            return False

    def get_ticket(self):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM ticket"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def update_ticket(self,ticket_id, event_name):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE ticket SET event_name = %s, registration_date = %s WHERE ticket_id = %s"
                cursor.execute(sql, (event_name, ticket_id))
                print(cursor.rowcount)
                connection.commit()
        except Exception as e:
            print(e)
            return False

    def delete_ticket(self, ticket_id):
        connection = self.connection
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM ticket WHERE ticket_id = %s"
                cursor.execute(sql, (ticket_id,))
                print(cursor.rowcount)
                connection.commit()
        except Exception as e:
            print(e)
            return False
