from typing import List
from uuid import UUID

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.vacancy import VacancyCreate, Vacancy
from api.utils.vacancies import get_recommended_vacancies, get_vacancy, get_vacancies, create_vacancy

router = fastapi.APIRouter()


@router.get("/vacancies", response_model=List[Vacancy], tags=["vacancies"])
async def read_vacancys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vacancys = get_vacancies(db, skip=skip, limit=limit)
    return vacancys


@router.post("/vacancies", response_model=Vacancy, status_code=201, tags=["vacancies"])
async def create_new_vacancy(vacancy: VacancyCreate, db: Session = Depends(get_db)):
    return create_vacancy(db=db, vacancy=vacancy)


@router.get("/vacancies/{VacancyId}", response_model=Vacancy, tags=["vacancies"])
async def read_vacancy(VacancyId: UUID, db: Session = Depends(get_db)):
    db_vacancy = get_vacancy(db=db, VacancyId=VacancyId)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy

@router.patch("/vacancies/{VacancyId}", response_model=Vacancy, tags=["vacancies"])
async def update_vacancy(VacancyId: UUID, vacancy: VacancyCreate, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")

@router.delete("/vacancies/{VacancyId}", response_model=Vacancy, tags=["vacancies"])
async def delete_vacancy(VacancyId: UUID, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")

@router.get("/recommendedVacancies/{UserId}", response_model=List[Vacancy], tags=["recommendedVacancies"])
async def recommended_vacancies(UserId: UUID, db: Session = Depends(get_db)):
    vacancys = get_recommended_vacancies(db, UserId=UserId)
    return vacancys