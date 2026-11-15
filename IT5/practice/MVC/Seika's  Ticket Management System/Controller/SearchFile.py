from MVC.FileHandler.File import FileHandler
class SearchTicket:
    def __init__(self, tickets):
        self.tickets = tickets
        self.file_handler = FileHandler()

    def search_ticket(self, ticket_id):
        tickets = self.file_handler.read_file()
        for ticket in tickets:
            field = ticket.strip().split(",")
            if int(field[2]) == ticket_id:
                return ticket.strip()
        return "Not Found"
