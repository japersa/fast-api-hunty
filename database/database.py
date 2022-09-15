from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://ixhiyccoqidofa:bc753cad64a0d32b7062b0cc8d64f109094f1c48f69348e27ce957b4106faf23@ec2-3-224-8-189.compute-1.amazonaws.com:5432/d7vbt1j3j3110j"
#SQLALCHEMY_DATABASE_URL = "postgresql://fastapi_hunty:fastapi_hunty@db:5432/fastapi_hunty"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()