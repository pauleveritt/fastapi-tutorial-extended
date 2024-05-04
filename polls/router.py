from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from polls.database import engine
from polls.models import Question

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/api/questions/")
def create_question(question: Question):
    with Session(engine) as session:
        session.add(question)
        session.commit()
        session.refresh(question)
        return question


@router.get("/api/questions/")
def read_questions():
    with Session(engine) as session:
        questions = session.exec(select(Question)).all()
        return questions


@router.get("/questions/{question_id}", response_class=HTMLResponse)
async def read_question_html(request: Request, question_id: str):
    with Session(engine) as session:
        question = session.exec(select(Question).where(Question.id == question_id))
        context = dict(question=question.one())
        return templates.TemplateResponse(
            request=request, name="item.html", context=context
        )


@router.get("/api/questions/{id}")
async def read_question_json(request: Request, id: str):
    with Session(engine) as session:
        question = session.exec(select(Question).where(Question.id == id))
        return question.one()
