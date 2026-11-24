from pydantic import BaseModel, Field

class StadentCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=0, lt=100)
    course : str = Field(min_length=2)

class StadentUpdate(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=0, lt=100)
    course : str = Field(min_length=2)
