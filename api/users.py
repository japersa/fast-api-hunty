from typing import List
from uuid import UUID

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.user import UserCreate, User
from api.utils.users import get_user, get_user_by_email, get_users, create_user

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User], tags=["users"])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201, tags=["users"])
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.Email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db=db, user=user)


@router.get("/users/{UserId}", response_model=User, tags=["users"])
async def read_user(UserId: UUID, db: Session = Depends(get_db)):
    db_user = get_user(db=db, UserId=UserId)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.patch("/users/{UserId}", response_model=User, tags=["users"])
async def update_user(UserId: UUID, user: UserCreate, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")

@router.delete("/users/{UserId}", response_model=User, tags=["users"])
async def delete_user(UserId: UUID, db: Session = Depends(get_db)):
   return HTTPException(status_code=500, detail="Method not immplement")
