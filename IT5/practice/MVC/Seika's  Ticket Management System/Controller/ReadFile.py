from MVC.FileHandler.File import FileHandler

class ReadTicket:
    def __init__(self):
        self.file_handler = FileHandler()

    def read_ticket(self):
        return self.file_handler.read_file()
