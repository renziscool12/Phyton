from MVC.FileHandler.File import FileHandler
class DeleteTicket:
    def __init__(self, tickets):
        self.tickets = tickets
        self.file_handler = FileHandler()

    def delete_ticket(self, ticket_id):
        tickets = self.file_handler.read_file()
        for ticket in tickets:
            field = ticket.strip().split(",")
            if int(field[2]) == ticket_id:
                tickets.remove(ticket)
                self.file_handler.update_file(tickets)
                return  "ticket has been deleted"

        return "Ticket not found!"
