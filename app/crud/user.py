from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserCrud:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        fake_hashed_password = user.password + 'notreallyhashed'
        db_user = User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
        return user
