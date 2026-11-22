class Person:
    def __init__(self, person_id, first_name, last_name):
        self._id = person_id
        self._first_name = first_name
        self._last_name = last_name

    @property
    def id(self):
        return self._id

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
