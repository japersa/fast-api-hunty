from tokenize import Name
from uuid import UUID
from sqlalchemy.orm import Session

from database.models.skill import Skill
from schemas.skill import SkillCreate


def get_skill(db: Session, SkillId: UUID):
    return db.query(Skill).filter(Skill.SkillId == SkillId).first()

def get_skill_by_name(db: Session, name: str):
    return db.query(Skill).filter(Skill.Name == name).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Skill).offset(skip).limit(limit).all()


def create_skill(db: Session, skill: SkillCreate):
    db_skill = Skill(Name=skill.Name)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill
