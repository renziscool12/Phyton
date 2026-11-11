from MVC.Controller.add_student import AddStudent
from  MVC.Controller.read_student import ReadStudent
from MVC.Controller.update_student import UpdateStudent
from MVC.Controller.delete_student import DeleteStudent
from MVC.Controller.seach_student import SearchStudent
from MVC.View.view import MenuView
from MVC.FileHandling.File import FileHandler

def main():
    files = FileHandler()
    add = AddStudent(files)

    add.student = files.read_student()

    students = add.student

    read = ReadStudent(files)
    update = UpdateStudent(students)
    delete = DeleteStudent(students, files)
    search = SearchStudent(students)

    view = MenuView(add, read, update, delete, search)
    view.menu()

if __name__ == "__main__":
    main()
