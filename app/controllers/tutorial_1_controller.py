from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/tutorials/1", response_class=HTMLResponse)
async def tutorial_1(request: Request):
    return templates.TemplateResponse(
        "tutorial_1.html",
        {
            "request": request,
            "title": "MERRILL Tutorial 1 – First model",
        },
    )

