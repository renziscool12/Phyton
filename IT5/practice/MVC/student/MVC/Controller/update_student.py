from MVC.FileHandling.File import FileHandler

class UpdateStudent:
    def __init__(self, students):
        self.students = students
        self.file_handler = FileHandler()

    def update_student(self, student_id, first_name=None, last_name=None, age=None, sex=None, courses=None):
        for student in self.students:
            if student.student_id == student_id:

                if first_name:
                    student.first_name = first_name
                if last_name:
                    student.last_name = last_name
                if age is not None:
                    student.age = age
                if sex:
                    student.sex = sex
                if courses is not None:
                    student.courses = courses

                self.file_handler.save_student(self.students)
                print(f"Student added successfully")
                return

        print(f"Student with id {student_id} not found")
