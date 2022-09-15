from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.orm import relationship

from ..database import Base
from .mixins import Timestamp

class Company(Timestamp, Base):
    __tablename__ = "companies"

    CompanyId = Column(postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    Name = Column(String(100), unique=True, index=True, nullable=False)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Phone = Column(String(20), nullable=False)
