class DeleteStudent:
    def __init__(self, students, file_handler):
        self.students =students
        self.file_handler = file_handler
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.file_handler.save_student(self.students)
                print(f"Student removed successfully")
                return

        print(f"Student with id {student_id} not found")
