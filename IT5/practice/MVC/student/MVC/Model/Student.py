from .Person import Person
from datetime import datetime

class Student(Person):
    def __init__(self, first_name, last_name, age, sex, student_id, courses, enrolled_time):
        super().__init__(first_name, last_name, age, sex)
        self._student_id = student_id
        self._courses = courses
        self._enrolled_time = enrolled_time

    @property
    def student_id(self):
        return self._student_id


    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses):
        self._courses = courses

    @property
    def enrolled_time(self):
        return self._enrolled_time

    @enrolled_time.setter
    def enrolled_time(self, value):
        self._enrolled_time = value

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.sex},{self.student_id}, {self.courses}, {self.enrolled_time}"
