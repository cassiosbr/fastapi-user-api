from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db, name: str, email: str):
        return self.user_repository.create(db, name, email)

    def get_user_by_email(self, db, email: str):
        return self.user_repository.get_by_email(db, email)

    def get_all_users(self, db):
        return self.user_repository.get_all(db)