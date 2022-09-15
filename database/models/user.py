from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.orm import relationship


from ..database import Base
from .mixins import Timestamp

class User(Timestamp, Base):
    __tablename__ = "users"

    UserId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=True)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    YearsPreviousExperience = Column(Integer, nullable=False)
    UserSkills = relationship("UserSkill", back_populates="User")
