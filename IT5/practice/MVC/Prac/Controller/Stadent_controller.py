from fastapi import HTTPException
from Model.Stadent_Model import StadentModel

class StadentController:
    def __init__(self):
        self.stadent_model = StadentModel()


    def get_all_stadents(self):
        return self.stadent_model.get_all_stadent()

    def get_stadent_by_id(self,stadent_id):
        result = self.stadent_model.get_stadent_by_id(stadent_id)

        if not result:
            return None
        return result

    def add_stadent(self, first_name, last_name, age, course):
        existing = self.stadent_model.get_stadent_by_name(first_name, last_name)
        if existing:
            raise HTTPException(status_code=409, detail="Stadent with that name already exists")
        stadent_id = self.stadent_model.add_stadent(first_name, last_name, age, course)
        return {"message": "Student added successfully", "stadent_id": stadent_id}

    def update_stadent(self, stadent_id, first_name, last_name, age, course):
        return self.stadent_model.update_stadent(first_name, last_name, age, course, stadent_id)

    def delete_stadent(self, stadent_id):
       return self.stadent_model.delete_stadent(stadent_id)

