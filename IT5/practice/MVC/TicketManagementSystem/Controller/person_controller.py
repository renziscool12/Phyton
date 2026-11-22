from TicketManagement.Model.Person_Model import PersonModel


class PersonController:
    def __init__(self):
        self.person_model = PersonModel()


    def add_person(self, first_name, last_name):
        if not first_name or not last_name:
            return False, "Name cannot be empty"
        result = self.person_model.add_person(first_name, last_name)
        if result:
            return True, "Person successfully added"
        return False, "Person already exists"

    def get_person(self):
        person = self.person_model.get_person()

        if person is None:
            return False, "Person not found"
        return True, person

    def update_person(self, person_id,first_name, last_name):
        if not first_name or not last_name:
            return False, "Name cannot be empty"

        result = self.person_model.update_person(person_id,first_name, last_name)

        if result:
            return True, "Person successfully updated"
        return False, "Person already exists"

    def delete_person(self, person_id):
        if not person_id:
            return False, "Person not found"

        if person_id <= 0:
            return False, "Person not found"
        result = self.person_model.delete_person(person_id)
        if result:
            return True, "Person successfully deleted"
        return False, "Person not found"
