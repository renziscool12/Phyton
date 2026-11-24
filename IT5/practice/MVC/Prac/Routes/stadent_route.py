from fastapi import APIRouter, HTTPException
from Controller.Stadent_Controller import StadentController
from Schemas.stadent_schemas import StadentCreate, StadentUpdate


router = APIRouter()
controller = StadentController()

@router.get('/')
def home():
    return {"message": "API is running!"}

@router.get('/stadent/')
def get_stadent():
    return controller.get_all_stadents()

@router.get('/stadent/{stadent_id}')
def get_stadent_by_stadent_id(stadent_id: int):
    stadent = controller.get_stadent_by_id(stadent_id)
    if not stadent:
        raise HTTPException(status_code=404, detail="Stadent not found")
    return stadent

@router.post('/stadent/')
def create_stadent(stadent:StadentCreate):
    return controller.add_stadent(stadent.first_name, stadent.last_name, stadent.age, stadent.course)

@router.put('/stadent/{stadent_id}')
def update_stadent(stadent_id: int, stadent:StadentUpdate):
    result = controller.update_stadent(stadent_id,stadent.first_name, stadent.last_name, stadent.age, stadent.course)

    if result == 0:
        raise HTTPException(status_code=404, detail="Stadent not found")
    return {"message": "Stadent updated successfully"}

@router.delete('/stadent/{stadent_id}')
def delete_stadent(stadent_id: int):
    result = controller.delete_stadent(stadent_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Stadent not found")
    return {"message": "Stadent deleted successfully"}
