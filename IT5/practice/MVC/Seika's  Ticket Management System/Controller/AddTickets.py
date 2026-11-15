from MVC.Model.Ticket import Ticket
from MVC.FileHandler.File import FileHandler
from datetime import datetime
class AddTicket:
    def __init__(self, tickets):
        self.tickets = tickets
        self.fileHandler = FileHandler()

    def add_ticket(self, first_name, last_name, ticket_id, event_name):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return "Ticket already exists"

        registration_date = datetime.now()
        ticket = Ticket(first_name, last_name, ticket_id, event_name, registration_date)
        self.tickets.append(ticket)
        self.fileHandler.save_file(self.tickets)
        return "Ticket created"
