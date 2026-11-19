from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Student API")

class StudentCreate(BaseModel):
    student_id: int = Field(gt=0)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    year_level: int = Field(ge=1, le=4)
    program: Literal["BSIT", "BSCS", "BSEMC", "BMA", "BLIS"]

students: dict[int, StudentCreate] = {}

@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/sudents")
def get_students():
    return list(students.values())

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.post("/students/", status_code=201)
def create_student(student: StudentCreate):
    if student.student_id in students:
        raise HTTPException(status_code=409, detail="Student ID exist")
    students[student.student_id] = student
    return student
