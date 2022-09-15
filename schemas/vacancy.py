from typing import List

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class RequiredSkillBase(BaseModel):
    SkillId: UUID
    RequiredSkillMinimumExperience: int

class VacancyBase(BaseModel):
    PositionName: str
    CompanyId: UUID
    VacancyLink: str
    Currency: str
    Salary : int

class VacancyCreate(VacancyBase):
    ...
    RequiredSkills: List[RequiredSkillBase]


class Vacancy(VacancyBase):
    VacancyId: UUID
    CreatedAt: datetime
    UpdatedAt: datetime
    RequiredSkills: List
    class Config:
        orm_mode = True


