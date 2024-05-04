from sqlmodel import Field, Relationship, Session, SQLModel, create_engine
from datetime import datetime


class Choice(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    choice_text: str
    votes: int = Field(default=0)
    question_id: int = Field(foreign_key="question.id")

    class Config:
        __table_args__ = {"extend_existing": True}


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question_text: str
    pub_date: datetime
    choices: list["Choice"] = Relationship(back_populates="question")

    def was_published_recently(self) -> bool:
        now = datetime.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
