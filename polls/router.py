from pathlib import Path

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import Session, select
from datetime import datetime
from polls.database import get_session, SessionLocal, engine
from polls.models import Question
from typing import List, Optional
from sqlalchemy import text

router = APIRouter()
package_dir = Path(__file__).parent.parent.absolute()
templates_dir = str(package_dir / "templates")
templates = Jinja2Templates(directory=templates_dir)


# Pydantic models for serialization
class Choice(BaseModel):
    choice_text: str


class QuestionWithChoices(BaseModel):
    question_text: str
    choices: List[Choice]


@router.post("/v1/question/")
def create_question(request_data: dict, session: Session = Depends(get_session)):
    from polls.models import Choice
    question_text = request_data.get("question_text")
    choices = request_data.get("choices")

    new_question = Question(question_text=question_text)
    session.add(new_question)
    session.commit()

    last_inserted_id = new_question.id

    for choice_text in choices:
        new_choice = Choice(choice_text=choice_text, question_id=last_inserted_id)
        session.add(new_choice)
    session.commit()

    return {"status": "ok", "message": "Question Added!"}


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
def patch_question(question_id: int, question: Question, session: Session = Depends(get_session)):
    db_patch_question = session.get(Question, question_id)
    if not db_patch_question:
        raise HTTPException(status_code=404, detail="Question not found")
    question_data = question.model_dump(exclude_unset=True)
    db_patch_question.sqlmodel_update(question_data)
    session.add(db_patch_question)
    session.commit()
    session.refresh(db_patch_question)
    return db_patch_question


@router.put("/v1/question/{question_id}", response_model=Question)
def put_question(question_id: int, question: Question, session: Session = Depends(get_session)):
    # Very similar to PATCH
    db_put_question = session.get(Question, question_id)
    if not db_put_question:
        raise HTTPException(status_code=404, detail="Question not found")
    question_data = question.model_dump(exclude_unset=True)
    db_put_question.sqlmodel_update(question_data)
    session.add(db_put_question)
    session.commit()
    session.refresh(db_put_question)
    return db_put_question


@router.delete("/v1/question/{question_id}")
async def delete_question(question_id: str, session: Session = Depends(get_session)):
    question = session.get(Question, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Update the question_id in choices to NULL
    for choice in question.choices:
        choice.question_id = None

    session.delete(question)
    session.commit()
    return {"ok": True}


# Questions, HTML
@router.get("/question/", response_class=HTMLResponse)
async def read_questions_html(request: Request, session: Session = Depends(get_session)):
    questions = session.exec(select(Question)).all()
    context = dict(questions=questions)
    return templates.TemplateResponse(
        request=request, name="questions.html", context=context
    )


@router.get("/question/{question_id}", response_class=HTMLResponse)
async def read_question_html(request: Request, question_id: str, session: Session = Depends(get_session)):
    question = session.exec(select(Question).where(Question.id == question_id))
    context = dict(question=question.one())
    return templates.TemplateResponse(
        request=request, name="question.html", context=context
    )

# Choices, API
