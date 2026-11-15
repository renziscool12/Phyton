from MVC.Controller.add_tickets import AddTicket
from MVC.Controller.read_ticket import ReadTicket
from MVC.Controller.delete_ticket import DeleteTicket
from MVC.Controller.update_ticket import UpdateTicket
from MVC.Controller.search_ticket import SearchTicket
from View.MenuTicket import MenuTicket

def main():
    tickets = []
    add_ticket = AddTicket(tickets)
    read_ticket = ReadTicket()
    delete_ticket = DeleteTicket(tickets)
    update_ticket = UpdateTicket(tickets)
    search_ticket = SearchTicket(tickets)

    menu_ticket = MenuTicket(add_ticket, read_ticket, update_ticket, delete_ticket, search_ticket)
    menu_ticket.main_menu()

if __name__ == "__main__":
    main()
