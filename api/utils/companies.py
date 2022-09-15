from tokenize import Name
from uuid import UUID
from sqlalchemy.orm import Session

from database.models.company import Company
from schemas.company import CompanyCreate

def get_company(db: Session, CompanyId: UUID):
    return db.query(Company).filter(Company.CompanyId == CompanyId).first()

def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.Name == name).first()

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(Name=company.Name, Email=company.Email, Phone=company.Phone)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
