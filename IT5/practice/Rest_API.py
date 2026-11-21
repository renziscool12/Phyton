from typing import Literal
from fastapi import FastAPI, HTTPException, Path, Response
from pydantic import BaseModel, ConfigDict, Field

Program = Literal["BSIT", "BSCS", "BSEMC", "BMA", "BLIS"]
app = FastAPI(title="Student REST API", version="1.0.0")

class StudentDetails(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    year_level: int = Field(ge=1, le=4)
    program: Program

class StudentCreate(StudentDetails):
        student_id: int = Field(gt=0)

students: dict[int, StudentCreate] = {}
@app.get("/")
def home():
    return {"message": "Student REST API is running"}

@app.get("/students", response_model=list[StudentCreate])
def get_students(program: Program):
    records = list(students.values())
    if program is not None:
        records = [s for s in records if s.program == program]
    return records

@app.get("/students/{student_id}", response_model=StudentCreate)
def get_student(student_id: int = Path(gt=0)):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    return students[student_id]

@app.post("/students/{student_id}", response_model=StudentCreate)
def create_student(student: StudentCreate):
    if student.student_id in students:
        raise HTTPException(409, "Student already exists")
    students[student.student_id] = student
    return student

@app.put("/students/{student_id}", response_model=StudentCreate)
def update_student(student: StudentDetails, student_id: int = Path(gt=0)):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    updated = StudentCreate(student_id=student_id, **student.model_dump())
    students[student_id] = updated
    return updated

@app.delete("/students/{student_id}", response_model=StudentCreate)
def delete_student(student_id: int = Path(gt=0)):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    del students[student_id]
    return Response(status_code=204)
