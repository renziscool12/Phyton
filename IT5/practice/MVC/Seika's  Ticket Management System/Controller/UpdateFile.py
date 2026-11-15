from MVC.FileHandler.File import FileHandler

class UpdateTicket:
    def __init__(self, tickets):
        self.tickets = tickets
        self.fileHandler = FileHandler()

    def update_ticket(self, first_name, last_name, ticket_id, event_name):
        tickets = self.fileHandler.read_file()
        for index, ticket in enumerate(tickets):
            fields = ticket.strip().split(",")
            if int(fields[2]) == ticket_id:
                fields[0] = first_name
                fields[1] = last_name
                fields[3] = event_name
                tickets[index] = ",".join(fields) + "\n"
                self.fileHandler.update_file(tickets)
                return "Ticket Updated Successfully"
        return "Ticket Not Found"
