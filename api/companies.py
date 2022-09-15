from typing import List
from uuid import UUID

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.company import CompanyCreate, Company
from api.utils.companies import get_company, get_companies, create_company, get_company_by_name

router = fastapi.APIRouter()


@router.get("/companies", response_model=List[Company], tags=["companies"])
async def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = get_companies(db, skip=skip, limit=limit)
    return companies


@router.post("/companies", response_model=Company, status_code=201, tags=["companies"])
async def create_new_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = get_company_by_name(db=db, name=company.Name)
    if db_company:
        raise HTTPException(status_code=400, detail="Name is already registered")
    return create_company(db=db, company=company)


@router.get("/companies/{CompanyId}", response_model=Company, tags=["companies"])
async def read_company(CompanyId: UUID, db: Session = Depends(get_db)):
    db_company = get_company(db=db, CompanyId=CompanyId)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.patch("/companies/{CompanyId}", response_model=Company, tags=["companies"])
async def update_company(CompanyId: UUID, company: CompanyCreate, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")


@router.delete("/companies/{CompanyId}", response_model=Company, tags=["companies"])
async def delete_company(CompanyId: UUID, db: Session = Depends(get_db)):
    return HTTPException(status_code=500, detail="Method not immplement")
