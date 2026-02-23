from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:

    def create(self, db: Session, name: str, email: str):
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_all_users(self, db: Session):
        return db.query(User).all()

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()