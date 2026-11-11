class SearchStudent:
    def __init__(self, students):
        self.students = students

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
