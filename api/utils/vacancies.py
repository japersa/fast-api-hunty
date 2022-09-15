from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.required_skill import RequiredSkill
from database.models.user import User

from database.models.vacancy import Vacancy
from schemas.vacancy import VacancyCreate


def get_vacancy(db: Session, VacancyId: UUID):
    return db.query(Vacancy).join(Vacancy.RequiredSkills).filter(Vacancy.VacancyId == VacancyId).first()


def get_vacancies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vacancy).join(Vacancy.RequiredSkills).offset(skip).limit(limit).all()

def get_recommended_vacancies(db: Session, UserId: UUID):
    """
        SELECT va."VacancyId", u."UserId"
        FROM  public.users u
        CROSS JOIN public.vacancies va 
        LEFT OUTER JOIN public.required_skills rs ON va."VacancyId" = rs."VacancyId"
        LEFT OUTER JOIN public.user_skills us ON u."UserId" = us."UserId" AND rs."SkillId" = us."SkillId" AND us."UserSkillExperience" >= rs."RequiredSkillMinimumExperience" 
        GROUP BY va."VacancyId", u."UserId"
        HAVING ((COUNT(DISTINCT us."SkillId") / COUNT(DISTINCT rs."SkillId")) * 100)  >= 50
    """
    vacancies = db.query(Vacancy).join(Vacancy.RequiredSkills).all()
    user = db.query(User).join(User.UserSkills).filter(User.UserId == UserId).first()
    recommended_vacancies = []
    for vacancy in vacancies:
        recommended_vacancies.append(vacancy)

    return recommended_vacancies

def create_vacancy(db: Session, vacancy: VacancyCreate):
    db_vacancy = Vacancy(PositionName=vacancy.PositionName, CompanyId= vacancy.CompanyId, Salary=vacancy.Salary, Currency=vacancy.Currency, VacancyLink=vacancy.VacancyLink)
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)

    for requiredSkill in vacancy.RequiredSkills:
        db_required = RequiredSkill(SkillId=requiredSkill.SkillId, RequiredSkillMinimumExperience= requiredSkill.RequiredSkillMinimumExperience, VacancyId=db_vacancy.VacancyId)
        db.add(db_required)
        db.commit()
        db.refresh(db_required)

    return db.query(Vacancy).join(Vacancy.RequiredSkills).filter(Vacancy.VacancyId == db_vacancy.VacancyId).first()
