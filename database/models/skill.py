from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from database.models.required_skill import RequiredSkill

from ..database import Base
from .mixins import Timestamp

class Skill(Timestamp, Base):
    __tablename__ = "skills"

    SkillId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    Name = Column(String(100), unique=True, index=True, nullable=False)
    RequiredSkills = relationship("RequiredSkill", back_populates="Skill")
    UserSkills = relationship("UserSkill", back_populates="Skill")

