from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import Session, select

from polls.database import get_session
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
def create_question(question: Question, session: Session = Depends(get_session)):
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


@router.get("/v1/question/")
def read_questions(session: Session = Depends(get_session)):
    questions = session.exec(select(Question)).all()
    return questions


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


@router.patch("/v1/question/{question_id}", response_model=Question)
def update_hero(question_id: int, question: Question, session: Session = Depends(get_session)):
    db_hero = session.get(Question, question_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    question_data = question.model_dump(exclude_unset=True)
    db_hero.sqlmodel_update(question_data)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@router.delete("/v1/question/{question_id}")
async def delete_question(question_id: str, session: Session = Depends(get_session)):
    question = session.get(Question, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    session.delete(question)
    session.commit()
    return {"ok": True}


# Questions, HTML

@router.get("/question/{question_id}", response_class=HTMLResponse)
async def read_question_html(request: Request, question_id: str, session: Session = Depends(get_session)):
    question = session.exec(select(Question).where(Question.id == question_id))
    context = dict(question=question.one())
    return templates.TemplateResponse(
        request=request, name="item.html", context=context
    )

# Choices, API
