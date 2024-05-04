from datetime import datetime, timedelta

from sqlmodel import Field, Relationship, SQLModel


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question_text: str
    pub_date: datetime
    choices: list["Choice"] = Relationship(back_populates="question")

    def was_published_recently(self) -> bool:
        now = datetime.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    choice_text: str
    votes: int = Field(default=0)
    question_id: int = Field(foreign_key="question.id")
    question: Question | None = Relationship(back_populates="choices")



