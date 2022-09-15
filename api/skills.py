from typing import List
from uuid import UUID

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.skill import SkillCreate, Skill
from api.utils.skills import get_skill, get_skills, create_skill, get_skill_by_name

router = fastapi.APIRouter()


@router.get("/skills", response_model=List[Skill], tags=["skills"])
async def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = get_skills(db, skip=skip, limit=limit)
    return skills


@router.post("/skills", response_model=Skill, status_code=201, tags=["skills"])
async def create_new_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = get_skill_by_name(db=db, name=skill.Name)
    if db_skill:
        raise HTTPException(status_code=400, detail="Name is already registered")
    return create_skill(db=db, skill=skill)


@router.get("/skills/{SkillId}", response_model=Skill, tags=["skills"])
async def read_skill(SkillId: UUID, db: Session = Depends(get_db)):
    db_skill = get_skill(db=db, SkillId=SkillId)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@router.patch("/skills/{SkillId}", response_model=Skill, tags=["skills"])
async def update_skill(SkillId: UUID, skill: SkillCreate, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")


@router.delete("/skills/{SkillId}", response_model=Skill, tags=["skills"])
async def delete_skill(SkillId: UUID, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")
