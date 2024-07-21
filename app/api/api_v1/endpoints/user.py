from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud.user import UserCrud
from app.db.database import get_db
from app.schemas.user import User, UserCreate

router = APIRouter()


@router.get('/', response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    return UserCrud().get_users(db=db, skip=0, limit=10)


@router.get('/{user_id}', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserCrud().get_user(db=db, user_id=user_id)


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserCrud().create_user(db=db, user=user)


@router.delete('/{user_id}', response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserCrud().delete_user(db=db, user_id=user_id)
