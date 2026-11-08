from model.Person import Person

class Staff(Person):
    def __init__(self, first_name, last_name, contact_number, email, sex, id):
        super().__init__(first_name, last_name, contact_number, email, sex)
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
