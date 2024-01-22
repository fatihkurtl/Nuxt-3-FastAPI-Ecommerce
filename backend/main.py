from fastapi import FastAPI
from app.products.models import models
from middlewares.cors import cors_settings
from db.database import engine
from routes import products

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


cors_settings()

app.include_router(products.router)

@app.get('/')
def home():
    return {
        'message': 'we are in home page'
    }