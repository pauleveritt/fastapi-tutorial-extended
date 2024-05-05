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

*Important note: Some features expect the database to have the seed content. Before demos, stop the server and
delete `database.db`, then restart.*

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
- Run the `FastAPI Server` run configuration
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
    - Click fourth endpoint `/v1/question/ GET`
        - Run the HTTP Client to test it
- Shift-Shift question_id and click the `Endpoints` tab
- Open `static/site.js` and show autocomplete of URL

## SPA Frontend

- Go to `package.json` and run `start` script
- Click the link
- Option-Cmd-O to Navigate to Symbol `App`
- Remove the import of `Index`
- Autocomplete the usage and show the import, then navigate to it
- Go to `className` and start adding `ca-a`
- Hover over the second choice (the Tailwind one) to preview the Tailwind class
- Escape to not add it
- Right-click on `src` and choose `Run tests` to see Vitest testing
- Double-click the first test to open
- Change `3` to `2`
- Click gutter icon to run just that test
- Mouse-over the `.length` assertion to see inlay with error info
- Set a breakpoint on that line
- Run test under the debugger

## pytest

- Right-click on `tests` directory and choose `Run`
- Double-click on `test_read_questions_json` and set a breakpoint on `data =` line
- Click gutter icon to debug that one test
- Remove breakpoint
- Click continue
- Open `polls.router.read_questions`
- Set a breakpoint on `questions =`
- Re-run test under debugger
- Step over and see what is returned

## HTTP Files

- With server running NOT in debug
- Open `run-apis.http`
- Click the `>>` green arrows at top to run all the tests
- Open `polls.router.read_questions`
- Set a breakpoint on `questions =`
- Stop the server and run it under the debugger
- Click the `>>` green arrows
- Execution stops on that route

## External Tools (Prettier, Black)

- Show the settings/preferences that configure both
- Make a change in some Python and save, showing that it reformats
- Same in `App.jsx`

## Docker

- Normal Dockerfile stuff