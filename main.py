from fastapi import FastAPI

from api import users, vacancies, companies, skills
from database.database import engine
from database.models import required_skill, skill, user, vacancy, user_skills, company

company.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
vacancy.Base.metadata.create_all(bind=engine)
skill.Base.metadata.create_all(bind=engine)
user_skills.Base.metadata.create_all(bind=engine)
required_skill.Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Fast API Hunty",
    description="API for managing users and vacancies.",
    version="1.0.0",
    contact={
        "name": "Alvaro Javier Perez Salcedo",
        "email": "japersa92@gmail.com",
    },
)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
    
app.include_router(companies.router)
app.include_router(skills.router)
app.include_router(users.router)
app.include_router(vacancies.router)
