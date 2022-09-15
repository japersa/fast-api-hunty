from uuid import UUID
from sqlalchemy.orm import Session

from database.models.user import User
from database.models.user_skills import UserSkill
from schemas.user import UserCreate


def get_user(db: Session, UserId: UUID):
    return db.query(User).join(User.UserSkills).filter(User.UserId == UserId).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.Email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).join(User.UserSkills).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(FirstName=user.FirstName, LastName= user.LastName, Email=user.Email, YearsPreviousExperience=user.YearsPreviousExperience)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    for userSkill in user.UserSkills:
        db_userSkill = UserSkill(SkillId=userSkill.SkillId, UserSkillExperience= userSkill.UserSkillExperience, UserId=db_user.UserId)
        db.add(db_userSkill)
        db.commit()
        db.refresh(db_userSkill)

    return db.query(User).join(User.UserSkills).filter(User.UserId == db_user.UserId).first()


