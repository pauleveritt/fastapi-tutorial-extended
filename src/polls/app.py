from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from polls.seed import initialize_table
from sqlalchemy import event



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


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # create database models.
    SQLModel.metadata.create_all(engine)
    yield


# Iterate over all tables and attach the event listener
for table in SQLModel.metadata.tables.values():
    event.listen(table, 'after_create', initialize_table)


app = FastAPI(lifespan=lifespan)


@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


@app.get("/heroes/")
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes
