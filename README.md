# FastAPI Tutorial Extended

A FastAPI implementation of the official Django tutorial, extended for PyCharm demo uses.

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
    - `Uvicorn options` as `--reload`
- Visit `http://127.0.0.1:8000/` and click `Questions` for the server HTML
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

### Running FastAPI Server

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


### Template Support

- `Shift-Shift pol/ind` to open `polls/index.html`
- On Line 12, insert new line and recreate the `<img src` with Emmet
    - `img tab` to start the `<img>` LiveTemplate
    - template for `{% s` to start the `static` Django tag
    - Autocomplete the part of the `polls/images/jb_beam.png` path
    - Make a typo to show squiggly
    - Fix typo
    - Cursor in the `jb_beam.png` segment
    - Cmd-B to navigate to the PNG

### Test-First

- `Cmd-Shift-A Spl Ri` to split right
- On left: `Cmd-Alt-O IndV` to navigate to IndexView
- On right: `Cmd-Alt-O t_p` to navigate to `tests/test_base_functions.test_polls_index`
- Click the gutter icon to run just that test
- On left: put a breakpoint in `IndexView.get_queryset`
- In test, click gutter icon and run in debug mode

### Git Pull Request Integration

TODO We need to file a PR.

### Fullstack: HTTP Files against Django Rest Framework

- Make sure Django Server is running _in debug mode_
- Open `run-apis.http`
- Run the first URL
- Put a breakpoint in `IndexView.get_queryset` on the `return`
- Click that URL again
- Continue, clear breakpoint

### Fullstack: Tailwind

- `base.html` and `<script src="https://cdn.tailwindcss.com">`
- We downloaded the "library" with Alt-Enter
- Go to `<div class="navbar` and autocomplete `navbar`
- Then, navigate to `navbar` to see definition

### Fullstack: React frontend

- In `package.json`, run the `dev` script
- Click the URL
- See the React app
- Navigate to Symbol `App`
- Remove the import of `Index`
- Autocomplete the usage and show the import, then navigate to it

### Fullstack: Prettier and eslint

- Mention `package.json` and npm integration
    - You get a popup with link for installing
    - Autocomplete in package.json
- In preferences, show Prettier integration
- Make sure prettier on save and reformat are checked
- In `Index.jsx` mess up spacing, indentation
- Reformat Code
- Show preferences for eslint

### Fullstack: React testing

- In `Index.jsx` put a breakpoint on `{question.question_text}`
- Split Right
- Shift-Shift `Index.tes` to navigate to the test file
- Use gutter icon to run test under the debugger

### Fullstack: Database tool

- Open the database tool
- Double-click on the `polls_question` table

## Extended Demo

This goes before the full-stack part and covers material
from [Adam's "Boost Your Django DX" book](https://adamchainz.gumroad.com/l/byddx).

### Inline documentation

- In `IndexView.get_queryset` mouse over:
    - `import` for Python code
    - `filter` for Django code
- Mouseover an `h1` to show MDN-integrated docs

### Virtual environments (covered)

### Package management

- Open `requirements.txt`
- Add another package
- Mention the community plugin
- Show it in action

### ipython

- Cmd-Shift-A Py Con
- Opens Python Console, with Django imports, using ipython
- Note the different repl
- `print(2+2)` with syntax highlighting, autocomplete

### EditorConfig

- Make sure `BlackConnect` is off!
- Open `.editorconfig`
- Change `4` to `14`
- Open `conftest.py`
- Reformat Code
- Change `14` back to `4`
- Reformat Code

### Black

- Enable BlackConnect

### pre-commit

- Note the `.pre-commit-config.yaml`
- Commit window, gear icon at bottom, show the checkbox for git hooks

### Testing (covered)

This will be used in the sponsor talk at PyCon US 2023.
It emphasizes points made in Adam Johnson's Django DX book.
