class FileHandler:

    def save_student(self, students):
        with open('students.txt', 'w') as file:
            for student in students:
                file.write(str(student) + "\n")

    def read_student(self):
        try:
            with open('students.txt', 'r') as file:
                return file.readlines()

        except FileNotFoundError:
            return []
