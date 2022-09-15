from typing import List

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SkillBase(BaseModel):
    Name: str

class SkillCreate(SkillBase):
    ...


class Skill(SkillBase):
    SkillId: UUID
    CreatedAt: datetime
    UpdatedAt: datetime

    class Config:
        orm_mode = True


