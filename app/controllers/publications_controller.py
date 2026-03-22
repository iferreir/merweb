from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.db.database import get_db
from app.db import models

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/publications", response_class=HTMLResponse)
async def publications(request: Request):
    with get_db() as db:
        pubs = (
            db.query(models.Publication)
            .order_by(models.Publication.year.desc())
            .all()
        )

    return templates.TemplateResponse(
        "publications.html",
        {
            "request": request,
            "title": "MERRILL – Publications",
            "publications": pubs,
        },
    )
