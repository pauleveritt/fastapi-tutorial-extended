from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def get_session():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

def get_session():
    with Session(engine) as session:
        yield session
