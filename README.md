# Candidate Application API [🏡](https://github.com/barronbytes/candidate-application-api)

This is a job application portal that uses FastAPI to handle job search queries and submissions.

## Tech Stack [🔝](#candidate-application-api-)

* **Frontend:** N/A
* **Backend:** Python, FastAPI
* **Database:** SQLite, SQLAlchemy

_Testing performed with unittest_

## Project Structure [🔝](#candidate-application-api-)

``` bash
candidate-application-api/
├── LICENSE                     # Project license (MIT)
├── .gitignore            
├── README.md
├── schema_job.py               # Schemas (Pydantic objects)
├── schema_application.py
├── model_apps_jobs.db          # Models (ORM objects)
├── model_database.py
├── model_table_job.py
├── model_table_application.py
├── service_job.py              # Services (CRUD functions)
├── service_application.py
├── routes.py                   # Routes (API endpoints)
├── main.py                     # App entry point
├── test_app.py                 # Unit test file


# Before running this project locally, ensure you have the following installed:
* IDE (VS Code, PyCharm, etc.)
* Install Python 3.10+ version > visit https://www.python.org/downloads/


# Install dependencies
pip install pydantic
pip install email-validator
pip install fastapi
pip install SQLAlchemy
pip install uvicorn
```

## Data Overview

This project contained a one-to-many relationship between jobs and applications, respectively.