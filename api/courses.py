from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Modelo Pydantic para Course
class Course(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    instructor: str

# Lista simulada de cursos
courses = []

@router.get("/courses", response_model=List[Course])
async def get_courses():
    """Obtém a lista de todos os cursos"""
    return courses

@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int):
    """Obtém um único curso pelo ID"""
    for course in courses:
        if course.id == course_id:
            return course
    return {"error": "Curso não encontrado"}

@router.post("/courses", response_model=List[Course])
async def create_course(course: Course):
    """Cria um novo curso"""
    course.id = len(courses) + 1  # Simples geração de ID
    courses.append(course)
    return courses

@router.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: int, course: Course):
    """Atualiza um curso existente pelo ID"""
    for i, c in enumerate(courses):
        if c.id == course_id:
            courses[i] = course
            return course
    return {"error": "Curso não encontrado"}

@router.delete("/courses/{course_id}", response_model=List[Course])
async def delete_course(course_id: int):
    """Deleta um curso pelo ID"""
    global courses
    courses = [course for course in courses if course.id != course_id]
    return courses
