from datetime import datetime, timedelta

from sqlmodel import Field, Relationship, SQLModel, Column, TIMESTAMP, text


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question_text: str
    pub_date: datetime | None = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    ))
    choices: list["Choice"] = Relationship(back_populates="question")

    def was_published_recently(self) -> bool:
        now = datetime.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    choice_text: str
    votes: int = Field(default=0)
    question_id: int = Field(foreign_key="question.id", nullable=True)
    question: Question | None = Relationship(back_populates="choices")
