class FileHandler:
    def save_file(self, tickets):
        with open('tickets.txt', 'a') as f:
            for ticket in tickets:
                f.write(str(ticket) + '\n')

    def read_file(self):
        try:
            with open('tickets.txt', 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return  []

    def update_file(self, tickets):
        with open('tickets.txt', 'w') as f:
            for ticket in tickets:
                f.write(ticket.strip() + '\n')
