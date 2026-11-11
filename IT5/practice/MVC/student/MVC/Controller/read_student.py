class ReadStudent:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def read_student(self):
        students = self.file_handler.read_student()

        for student in students:
            print(student.strip())
