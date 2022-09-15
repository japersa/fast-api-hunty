from typing import List

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class UserSkillBase(BaseModel):
    SkillId: UUID
    UserSkillExperience: int

class UserBase(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    YearsPreviousExperience : int

class UserCreate(UserBase):
    ...
    UserSkills: List[UserSkillBase]

class User(UserBase):
    UserId: UUID
    CreatedAt: datetime
    UpdatedAt: datetime
    UserSkills: List

    class Config:
        orm_mode = True


