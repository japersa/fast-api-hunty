from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid

from sqlalchemy.orm import relationship

from ..database import Base
from .mixins import Timestamp

class UserSkill(Timestamp, Base):
    __tablename__ = "user_skills"

    UserSkillId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    UserSkillExperience = Column(Integer, nullable=False)
    UserId = Column(postgresql.UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    SkillId = Column(postgresql.UUID(as_uuid=True), ForeignKey("skills.SkillId"), nullable=False)
    User = relationship("User", back_populates="UserSkills")
    Skill = relationship("Skill", back_populates="UserSkills")