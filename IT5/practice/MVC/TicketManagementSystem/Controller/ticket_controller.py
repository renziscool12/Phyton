from TicketManagement.Model.Ticket_Model import TicketModel
from datetime import date

class TicketController:
    def __init__(self):
        self.ticket_model = TicketModel()

    def add_ticket(self, event_name):
        registration_date = date.today()
        if not event_name:
            return False, "Event name cannot be empty"

        result = self.ticket_model.add_ticket(event_name, registration_date)

        if result:
            return True, "Ticket added successfully"
        return False, "Ticket already exists"

    def get_ticket(self):
        ticket = self.ticket_model.get_ticket()

        if ticket:
            return False, "Ticket not found"
        return True, ticket

    def update_ticket(self, ticket_id, event_name):
        if not event_name:
            return False, "Event name cannot be empty"
        result = self.ticket_model.update_ticket(ticket_id, event_name)
        if result:
            return True, "Ticket updated successfully"
        return False, "Ticket does not exist"

    def delete_ticket(self, ticket_id):
        if ticket_id <= 0:
            return False, "Ticket id cannot be negative"

        result = self.ticket_model.delete_ticket(ticket_id)
        if result:
            return True, "Ticket deleted successfully"
        return False, "Ticket does not exist"
