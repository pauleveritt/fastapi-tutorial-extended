# FastAPI Tutorial Extended

A FastAPI implementation of the official Django tutorial, extended for PyCharm demo uses.

## Prerequisites

- Python 3.10+
- NodeJS

## Installation

- Clone this repo and go to the directory.
- `python -m venv .venv`
- `.venv/bin/pip install --upgrade pip`
- `.venv/bin/pip install -r requirements.txt`
- `npm install`
- `npm build`
- `npm css`
- Open PyCharm Professional
- Enable Prettier and Black support to run on save
- Settings | Languages & Frameworks | Node.js and check `Coding assistance...`
- Mark directories
    * `dist` as Excluded
    * `tests` as Test
    * `templates` as Templates
    * `static` as Static resources
- Settings | Languages & Frameworks | Template Languages, enable `Jinja2`
- Make a FastAPI run configuration
    - `Application file` as `polls/app.py`
    - `Uvicorn options` as `--reload --port 8080`
- Visit `http://127.0.0.1:8080/` and click `Questions` for the server HTML
- Go to `package.json` and run the `dev` script for the React frontend
    - Then click the URL in the run output
- Double-click on `database.db` to connect to SQLite
    - Install the drivers if needed

## Main Demo

We're going to talk about the "I" in "IDE".

### Project Setup

- PyCharm eliminates some cumbersome setup steps
- Show that you could use PyCharm's bundled `FastAPI` template in `New Project`
    - Makes and sets a virtual env
    - Installs FastAPI into it
    - Makes a sample FastAPI project
    - Creates run configuration

### Running/Debugging FastAPI Server

- Shift-Shift `tem/bas` to open `templates/base.html`
- Run the `Django Server` run configuration
- Click on link in the run window
- Navigate to `Questions`
    - Delete the `img` with `PyCharm.svg`
    - Save
    - Reload browser
    - See that FastAPI restarts the process
- Run server under the debugger, not a big speed hit
    - Stop the running server
    - Restart it with the debugger
    - Set breakpoint in:
        - `polls.router.read_questions_html`
        - Also in `templates/questions.html`
            - Inside `{% for question in questions %}`
    - Reload the page at `/question/`
    - Show stepping through Python and Jinja2
    - Clear the breakpoints and resume

## Database

- Double-click on `database.db`
- Browse to `question` table
- Double-click to open it
- Normal DataGrip demo stuff

## Endpoints

- Make sure FastAPI server is running
- Open endpoints tool and show the discovered endpoints
  - Click second endpoint `/question/ GET`
    - Run the HTTP Client to test it