
from model.Student import Student
from model.Staff import Staff
from view.shs_view import RegistrationView


class RegistrationController:
    def __init__(self):
        self.students = []
        self.staff_members = []
        self.view = RegistrationView()

    def add_student(self, first_name, last_name, contact_number, email, sex, id, date_registered):
        student = Student(first_name, last_name, contact_number, email, sex, id, date_registered)
        self.students.append(student)
        print(f"Student {first_name} {last_name} added successfully.")

    def add_staff(self, first_name, last_name, contact_number, email, sex, id):
        staff_member = Staff(first_name, last_name, contact_number, email, sex, id)
        self.staff_members.append(staff_member)
        print(f"Staff member {first_name} {last_name} added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("List of Students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Date Registered: {student.date_registered}")

    def view_staff(self):
        if not self.staff_members:
            print("No staff members found.")
            return

        print("List of Staff Members:")
        for staff_member in self.staff_members:
            print(f"ID: {staff_member.id}, Name: {staff_member.first_name} {staff_member.last_name}")

    def update_student(self, student_id, first_name=None, last_name=None):
        for student in self.students:
            if student.id == student_id:
                if first_name:
                    student.first_name = first_name
                if last_name:
                    student.last_name = last_name

                print(f"Student ID {student_id} updated successfully.")
                return

        print(f"Student ID {student_id} not found.")

    def update_staff(self, staff_id, first_name=None, last_name=None):
        for staff_member in self.staff_members:
            if staff_member.id == staff_id:
                if first_name:
                    staff_member.first_name = first_name
                if last_name:
                    staff_member.last_name = last_name

                print(f"Staff ID {staff_id} updated successfully.")
                return

        print(f"Staff ID {staff_id} not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print(f"Student ID {student_id} deleted successfully.")
                return

        print(f"Student ID {student_id} not found.")

    def delete_staff(self, staff_id):
        for staff_member in self.staff_members:
            if staff_member.id == staff_id:
                self.staff_members.remove(staff_member)
                print(f"Staff ID {staff_id} deleted successfully.")
                return

        print(f"Staff ID {staff_id} not found.")

    def run(self):
        while True:
            self.view.menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                contact_number = input("Enter contact number: ")
                email = input("Enter email: ")
                sex = input("Enter sex: ")
                id = input("Enter student ID: ")
                date_registered = input("Enter registration date: ")

                self.add_student(
                    first_name, last_name, contact_number,
                    email, sex, id, date_registered
                )

            elif choice == '2':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                contact_number = input("Enter contact number: ")
                email = input("Enter email: ")
                sex = input("Enter sex: ")
                id = input("Enter staff ID: ")

                self.add_staff(
                    first_name, last_name, contact_number,
                    email, sex, id
                )

            elif choice == '3':
                self.view_students()

            elif choice == '4':
                self.view_staff()

            elif choice == '5':
                student_id = input("Enter student ID to update: ")
                first_name = input("Enter new first name (leave blank to keep current): ")
                last_name = input("Enter new last name (leave blank to keep current): ")

                self.update_student(student_id, first_name or None, last_name or None)

            elif choice == '6':
                staff_id = input("Enter staff ID to update: ")
                first_name = input("Enter new first name (leave blank to keep current): ")
                last_name = input("Enter new last name (leave blank to keep current): ")

                self.update_staff(staff_id, first_name or None, last_name or None)

            elif choice == '7':
                student_id = input("Enter student ID to delete: ")
                self.delete_student(student_id)

            elif choice == '8':
                staff_id = input("Enter staff ID to delete: ")
                self.delete_staff(staff_id)

            elif choice == '9':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
