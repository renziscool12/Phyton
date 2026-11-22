from TicketManagement.Model.Person_Model import PersonModel
from TicketManagement.Model.Ticket_Model import TicketModel


class MainView:
    def __init__(self):
        self.ticket_model = TicketModel()
        self.person_model = PersonModel()


    def run(self):
        while True:
            print("\n---Seika Ticket Management---")
            print("1. Person Management")
            print("2. Ticket Management")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                print("Thank you for your time")
                break
            else:
                print("Invalid Choice")
                return

    def person_menu(self):
        while True:
            print("---Person Management---")
            print("1. Add Person")
            print("2. View People")
            print("3. Update Person")
            print("4. Delete Person")
            print("5. Back")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                break
            else:
                print("Invalid Choice")
                return
    def ticket_menu(self):
        pass

