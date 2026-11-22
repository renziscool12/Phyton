from TicketManagement.Model.Person import Person

class Ticket(Person):
    def __init__(self, person_id, first_name,last_name, ticket_id, event_name, registration_date):
        super().__init__(person_id,first_name, last_name)
        self._ticket_id = ticket_id
        self._event_name = event_name
        self._registration_date = registration_date

    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def event_name(self):
        return self._event_name

    @property
    def registration_date(self):
        return self._registration_date

    @event_name.setter
    def event_name(self, value):
        self._registration_date = value
