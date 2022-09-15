from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.orm import relationship

from schemas.skill import Skill

from ..database import Base
from .mixins import Timestamp

class RequiredSkill(Timestamp, Base):
    __tablename__ = "required_skills"

    RequiredSkillId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    RequiredSkillMinimumExperience= Column(Integer, nullable=False)
    VacancyId = Column(postgresql.UUID(as_uuid=True), ForeignKey("vacancies.VacancyId"), nullable=False)
    SkillId = Column(postgresql.UUID(as_uuid=True), ForeignKey("skills.SkillId"), nullable=False)

    Vacancy = relationship("Vacancy", back_populates="RequiredSkills")
    Skill = relationship("Skill", back_populates="RequiredSkills")