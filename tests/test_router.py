import pytest
from bs4 import BeautifulSoup
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from polls.app import app
from polls.database import get_session
from polls.models import Question
from polls.seed import questions_data


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_read_questions_json(client: TestClient):
    # Use the existing seed data
    response = client.get("/v1/question/")
    data = response.json()
    assert len(data) == len(questions_data)


def test_read_questions_html(client: TestClient):
    # Use the existing seed data
    response = client.get("/question/")
    assert response.status_code == 200
    html = BeautifulSoup(response.content, "html5lib")
    questions = html.select(".question_text a")
    assert len(questions) == len(questions_data)
    assert questions[0].attrs["href"] == "http://testserver/question/1"
    assert questions[0].text == questions_data[0]["question_text"]


def test_read_question_json(client: TestClient):
    # Use the existing seed data
    response = client.get("/v1/question/1")
    data = response.json()
    assert data["id"] == 1
    assert data["question_text"] == questions_data[0]["question_text"]


def test_create_question_json(client: TestClient):
    post_data = {"question_text": questions_data[0]["question_text"]}
    response = client.post("/v1/question/", json=post_data)
    data = response.json()
    assert data["question_text"] == post_data["question_text"]


def test_patch_question_json(client: TestClient, session: Session):
    # Load a question
    question = Question(question_text=questions_data[0]["question_text"])
    session.add(question)
    session.commit()

    response = client.patch(f"/v1/question/{question.id}", json={"question_text": "What?"})
    assert response.status_code == 200
    data = response.json()
    assert data["question_text"] == "What?"


def test_put_question_json(client: TestClient, session: Session):
    # Load a question
    question = Question(question_text=questions_data[0]["question_text"])
    session.add(question)
    session.commit()

    response = client.put(f"/v1/question/{question.id}", json={"question_text": "Who?"})
    assert response.status_code == 200
    data = response.json()
    assert data["question_text"] == "Who?"


def test_delete_question_json(client: TestClient, session: Session):
    # Load a question
    question = Question(question_text=questions_data[0]["question_text"])
    session.add(question)
    session.commit()

    response = client.delete(f"/v1/question/{question.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True
