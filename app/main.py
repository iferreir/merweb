from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.database import engine
from app.db import models

# Import controllers
from app.controllers.home_controller import router as home_router
from app.controllers.downloads_controller import router as downloads_router
from app.controllers.tutorials_controller import router as tutorials_router
from app.controllers.tutorial_1_controller import router as tutorial1_router
from app.controllers.publications_controller import router as publications_router


models.Base.metadata.create_all(bind=engine)

# Create app
app = FastAPI(title="MERRILL Website")

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Add controllers

app.include_router(home_router)
app.include_router(downloads_router)
app.include_router(tutorials_router)
app.include_router(publications_router)
app.include_router(tutorial1_router)

@app.get("/health")
async def health():
    return {"status": "MERRILL website ready!"}

