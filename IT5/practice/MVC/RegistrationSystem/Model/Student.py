from model.Person import Person

class Student(Person):
    def __init__(self, first_name, last_name, contact_number, email, sex, id, date_registered):
        super().__init__(first_name, last_name, contact_number, email, sex)
        self._id = id
        self._date_registered = date_registered

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def date_registered(self):
        return self._date_registered

    @date_registered.setter
    def date_registered(self, value):
        self._date_registered = value
