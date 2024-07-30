from pathlib import Path

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.polls.database import get_session
from app.polls.models import Question

router = APIRouter(prefix="/question")
package_dir = Path(__file__).parent.parent.absolute()
templates_dir = str(package_dir / "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/", response_class=HTMLResponse)
async def read_questions_html(
    request: Request, session: Session = Depends(get_session)
):
    questions = session.exec(select(Question)).all()
    context = dict(questions=questions)
    return templates.TemplateResponse(
        request=request, name="questions.html", context=context
    )


@router.get("/{question_id}", response_class=HTMLResponse)
async def read_question_html(
    request: Request, question_id: str, session: Session = Depends(get_session)
):
    question = session.exec(select(Question).where(Question.id == question_id))
    context = dict(question=question.one())
    return templates.TemplateResponse(
        request=request, name="question.html", context=context
    )


# Home page
@router.get("/", response_class=HTMLResponse)
async def index_html(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
