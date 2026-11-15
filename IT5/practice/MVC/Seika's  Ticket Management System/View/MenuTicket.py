class MenuTicket:
    def __init__(self, add_ticket, read_ticket, update_ticket, delete_ticket, search_ticket):
        self.add_controller = add_ticket
        self.read_controller = read_ticket
        self.update_controller = update_ticket
        self.delete_controller = delete_ticket
        self.search_controller = search_ticket

    def add_tickets(self):
        try:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            ticket_id = int(input("Ticket ID: "))
            event_name = input("Event Name: ")

            if not first_name or not last_name or not ticket_id or not event_name:
                print("Should not be empty")
                return
            tickets = self.add_controller.add_ticket(first_name, last_name, ticket_id, event_name)
            print(tickets)
        except ValueError:
            print("Invalid Input")
            return

    def read_tickets(self):
        read_ticket = self.read_controller.read_ticket()
        if not read_ticket:
            print("No tickets found")
        for ticket in read_ticket:
            print(ticket)

    def update_tickets(self):
        ticket_id = int(input("Ticket ID: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        event_name = input("Event Name: ")
        if not first_name or not last_name or not event_name:
            print("Should not be empty")
            return

        if first_name.isdigit() or last_name.isdigit():
            print("Must be String")
            return

        self.update_controller.update_ticket(first_name, last_name, ticket_id,event_name)

    def delete_tickets(self):
        try:
            ticket_id = int(input("Ticket ID: "))
            result = self.delete_controller.delete_ticket(ticket_id)
            print(result)
        except ValueError:
            print("Invalid Input")
            return


    def search_tickets(self):
        try:

            ticket_id = int(input("Ticket ID: "))
            searched = self.search_controller.search_ticket(ticket_id)
            print("Calling DeleteTicket...")
            result = self.delete_controller.delete_ticket(ticket_id)
            print(result)
            print(searched)
        except ValueError:
            print("Invalid Input")
            return

    def main_menu(self):
        while True:
            print("SEIKA'S STARRY TICKET MANAGEMENT SYSTEM\n")
            print("1. Add Ticket")
            print("2. Read Ticket")
            print("3. Update Ticket")
            print("4. Delete Ticket")
            print("5. Search Ticket")
            print("6. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_tickets()
            elif choice == 2:
                self.read_tickets()
            elif choice == 3:
                self.update_tickets()
            elif choice == 4:
                self.delete_tickets()
            elif choice == 5:
                self.search_tickets()
            elif choice == 6:
                print("Thank you for using this program")
                break
            else:
                print("Invalid Input")
