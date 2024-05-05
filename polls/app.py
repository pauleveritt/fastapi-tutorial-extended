from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

package_dir = Path(__file__).parent.parent.absolute()
static_dir = package_dir / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(common_router)
