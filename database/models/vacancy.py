from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.orm import relationship


from ..database import Base
from .mixins import Timestamp

class Vacancy(Timestamp, Base):
    __tablename__ = "vacancies"

    VacancyId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    PositionName = Column(String(100), nullable=False)
    CompanyId = Column(postgresql.UUID(as_uuid=True), ForeignKey("companies.CompanyId"), nullable=False)
    VacancyLink = Column(String(100), nullable=True)
    Currency = Column(String(100), nullable=True)
    Salary = Column(Integer, nullable=False)
    RequiredSkills = relationship("RequiredSkill", back_populates="Vacancy")
    