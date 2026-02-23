from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.routes import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"])