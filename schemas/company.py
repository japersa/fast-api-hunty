from typing import List

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CompanyBase(BaseModel):
    Name: str
    Email: str
    Phone: str

class CompanyCreate(CompanyBase):
    ...


class Company(CompanyBase):
    CompanyId: UUID
    CreatedAt: datetime
    UpdatedAt: datetime

    class Config:
        orm_mode = True


