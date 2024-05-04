from datetime import datetime, timedelta

from sqlmodel import Field, Relationship, SQLModel


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question_text: str
    pub_date: datetime
    # TODO When this is uncommented, fails for URL /questions/
    # choices: list["Choice"] = Relationship(back_populates="question")

    def was_published_recently(self) -> bool:
        now = datetime.now()
        return now - timedelta(days=1) <= self.pub_date <= now
