
class MenuView:
    def __init__(self, add_student, read_student,update_student, delete_student, search_student):
        self.add_controller = add_student
        self.read_controller = read_student
        self.update_controller = update_student
        self.delete_controller = delete_student
        self.search_controller = search_student

    def add_student(self):
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            age = int(input("Enter your age: "))
            sex = input("Enter your sex: ").lower()
            student_id = int(input("Enter your student ID: "))
            course = input("Enter your course: ")

            if sex not in ["male", "female"]:
                print("Invalid Sex!")
                return

            if first_name.isdigit() or last_name.isdigit():
                print("Invalid Input!")
                return

            if age < 0 or age > 100:
                print("Invalid Age!")
                return


            self.add_controller.add_student(first_name, last_name, age, sex, student_id,course)
        except ValueError:
            print("Invalid Input!")
            return

    def read_student(self):
        students =  self.read_controller.read_student()

        if not students:
            print("No Student Found!")
            return

        for student in students:
            print(student.strip())

    def update_student(self):
        try:
            student_id = int(input("Enter your student ID: "))
            first_name = input("Enter your new first name: ")
            last_name = input("Enter your new last name: ")
            age = int(input("Enter your new age: "))
            sex = input("Enter your new sex: ").lower()
            course = input("Enter your new course: ")

            if sex not in ["male", "female"]:
                print("Invalid Sex!")
                return

            if age < 0 or age > 100:
                print("Invalid Age!")
                return

            if first_name.isdigit() or last_name.isdigit():
                print("Invalid Input!")
                return

            self.update_controller.update_student(student_id, first_name, last_name, age, sex, course)
        except ValueError:
            print("Invalid Input!")
            return

    def delete_student(self):
        try:
            student_id = int(input("Enter the student ID to delete: "))
            if student_id <= 0:
                print("Invalid Student ID!")
                return

            self.delete_controller.delete_student(student_id)

        except ValueError:
            print("Invalid Input!")

    def search_student(self):
        try:
            student_id = int(input("Enter your student ID: "))
            if student_id <= 0:
                print("Invalid Student ID!")
                return
            student = self.search_controller.search_student(student_id)
            if student is None:
                print("No Student Found!")
            else:
                print(student)
        except ValueError:
            print("Invalid Input!")
            return

    def menu(self):
        while True:
            print("Student Menu\n")
            print("1. Add Student")
            print("2. Read Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Search Student")
            print("6. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.read_student()
            elif choice == 3:
                self.update_student()
            elif choice == 4:
                self.delete_student()
            elif choice == 5:
                self.search_student()
            elif choice == 6:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")


