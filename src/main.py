from fastapi import FastAPI
from src.core.config import settings
from src.db import base
from src.api.routes import user


app = FastAPI(
    title=settings.PROJECT_NAME , 
    version=settings.PROJECT_VERSION
)

app.include_router(user.router , prefix='/users' , tags=['Usuarios'])