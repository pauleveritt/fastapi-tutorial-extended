from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import Session, select

from polls.database import engine, get_session
from polls.models import Question

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Pydantic models for serialization
class Choice(BaseModel):
    id: int
    choice_text: str


class QuestionWithChoices(BaseModel):
    id: int
    question_text: str
    choices: list[Choice]


@router.post("/v1/question/")
def create_question(question: Question):
    with Session(engine) as session:
        session.add(question)
        session.commit()
        session.refresh(question)
        return question


@router.get("/v1/question/")
def read_questions(session: Session = Depends(get_session)):
    questions = session.exec(select(Question)).all()
    return questions


# @router.get("/v1/question/{id}")
# async def read_question_json(request: Request, id: str):
#     with Session(engine) as session:
#         question = session.exec(select(Question).where(Question.id == id))
#         return question.one()


@router.get("/v1/question/{question_id}", response_model=QuestionWithChoices)
def read_question_json(question_id: int, session: Session = Depends(get_session)):
    # Fetch the question by ID
    question = session.get(Question, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Load the related options (choices)
    session.refresh(question)

    # Convert the SQLModel objects to Pydantic models
    question_with_options = QuestionWithChoices(
        id=question.id,
        question_text=question.question_text,
        choices=[Choice(id=option.id, choice_text=option.choice_text) for option in question.choices]
    )
    return question_with_options


# Questions, HTML

@router.get("/question/{question_id}", response_class=HTMLResponse)
async def read_question_html(request: Request, question_id: str):
    with Session(engine) as session:
        question = session.exec(select(Question).where(Question.id == question_id))
        context = dict(question=question.one())
        return templates.TemplateResponse(
            request=request, name="item.html", context=context
        )
