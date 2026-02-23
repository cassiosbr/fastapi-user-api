from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.routes import user_routes, auth_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)