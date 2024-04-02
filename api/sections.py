from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Modelo Pydantic para Section
class Section(BaseModel):
    id: Optional[int] = None
    name: str
    course_id: int
    description: str

# Lista simulada de seções
sections = []

@router.get("/sections", response_model=List[Section])
async def get_sections():
    """Obtém a lista de todas as seções"""
    return sections

@router.get("/sections/{section_id}", response_model=Section)
async def get_section(section_id: int):
    """Obtém uma única seção pelo ID"""
    for section in sections:
        if section.id == section_id:
            return section
    return {"error": "Seção não encontrada"}

@router.post("/sections", response_model=List[Section])
async def create_section(section: Section):
    """Cria uma nova seção"""
    section.id = len(sections) + 1  # Simples geração de ID
    sections.append(section)
    return sections

@router.put("/sections/{section_id}", response_model=Section)
async def update_section(section_id: int, section: Section):
    """Atualiza uma seção existente pelo ID"""
    for i, s in enumerate(sections):
        if s.id == section_id:
            sections[i] = section
            return section
    return {"error": "Seção não encontrada"}

@router.delete("/sections/{section_id}", response_model=List[Section])
async def delete_section(section_id: int):
    """Deleta uma seção pelo ID"""
    global sections
    sections = [section for section in sections if section.id != section_id]
    return sections
