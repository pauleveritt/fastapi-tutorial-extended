from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import event
from sqlmodel import SQLModel

from polls.database import create_db_and_tables
from polls.router import router as common_router
from polls.seed import initialize_table


@asynccontextmanager
async def lifespan(this_app: FastAPI):
    # create database models.
    create_db_and_tables()
    yield


# Iterate over all tables and attach the event listener
for table in SQLModel.metadata.tables.values():
    event.listen(table, 'after_create', initialize_table)

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(common_router)
