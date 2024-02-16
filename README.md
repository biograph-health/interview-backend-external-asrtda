# Biograph Technical Interview

From the Biograph engineering team, thank you for your interest in a software 
engineering role. We are excited to meet you!

During one of your interviews, you will pair with an engineer on the team to add some
functionality to this pretend codebase. Our goal is to learn how you approach work 
that is similar in nature to what you may do at Biograph on a day-to-day basis.

At Biograph, we are primarily interested in building useful and delightful products.
That's what we are striving to assess here. We are not interested in quizzing you on
algorithms, and there are no trick questions. You'll be asked to make a series of
decisions without clear "right" or "wrong" answers. We hope this allows you to most 
effectively demonstrate how you collaborate and think through technical problems.

We want you to use whatever coding environment you are most comfortable with, so we
invite you to bring your own laptop to the interview. We'll ask you to share your
screen while you are writing code. Read through the rest of this document for a brief
introduction to the codebase and instructions on running and testing the application.

## The Codebase

We'll pretend that this codebase powers the reservation system at Rao's, a notoriously
difficult-to-get-into restaurant in New York City. The codebase is a simple JSON API 
with two resources: tables and reservations. The restaurant has a limited number of 
tables and each table has a certain number of seats. Reservations for a given table,
date, and time slot (5:30, 7:00, or 8:30) may be made under an email address. 

The following endpoints are available to start:

```plaintext
GET     /tables           GET     /reservations
POST    /tables           POST    /reservations
GET     /tables/{id}      GET     /reservations/{id}
DELETE  /tables/{id}      DELETE  /reservations/{id}
```

We use [FastAPI](https://fastapi.tiangolo.com/) to power the API. We chose FastAPI
because it provides documentation and testing with minimal boilerplate code. We are
not trying to assess framework knowledge. You may consult your interviewer on the 
tech stack at any time.

## Getting Started

We use [Poetry](https://python-poetry.org/) to manage dependencies and provide an
isolated runtime environment. Poetry requires Python 3.8+ and should be installed in 
an isolated virtual environment. Please follow these platform-specific installation
instructions:

 - https://python-poetry.org/docs/#installation

Once Poetry is installed on your system, you can install the project's dependencies 
by running the following command in the root of the project:

```bash
poetry install
```

This will create a new virtual environment for this project. You can then run the API
in the virtual environment with the following command:

```bash
poetry run uvicorn app.main:app --reload
```

This will start the server on http://127.0.0.1:8000. You can access interactive
OpenAPI documentation at http://127.0.0.1:8000/docs.

We use pytest for our test suite. You can run the tests with the following command:

```bash
poetry run pytest -v .
```

Once you are able to run and test the app, your setup is complete.