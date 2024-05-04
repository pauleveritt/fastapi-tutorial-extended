from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from sqlmodel import select, create_engine, SQLModel
from polls.seed import initialize_table
from sqlalchemy import event
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .models import Question, Choice, Hero

from polls.router import router as common_router

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
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



app.include_router(common_router)



