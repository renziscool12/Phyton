from MVC.Model.Student import Student
from datetime import date

class AddStudent():
    def __init__(self, file_handler):
        self.student = []
        self.file_handler = file_handler


    def add_student(self,first_name, last_name, age, sex, student_id, courses):
        for student in self.student:
            if student.student_id == student_id:
                print("Student already exists!")
                return

        enrolled_time = date.today()
        student = Student(first_name, last_name, age, sex, student_id, courses, enrolled_time)
        self.student.append(student)
        self.file_handler.save_student(self.student)
        print(f"Student added successfully")
