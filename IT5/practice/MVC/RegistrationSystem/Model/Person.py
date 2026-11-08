class Person:
    def __init__(self, first_name, last_name, contact_number, email, sex):
        self._first_name = first_name
        self._last_name = last_name
        self._contact_number = contact_number
        self._email = email
        self._sex = sex

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        
