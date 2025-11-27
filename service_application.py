from sqlalchemy.orm import Session
from schema_application import Application, ApplicationCreate
from model_table_application import Application as ApplicationTable


def create_application(application: ApplicationCreate, db: Session) -> Application:
    """
    Saves new job applicant data from a person (Pydantic ApplicationCreate schema object)
    to be saved as a new record in the application table (SQLAlchemy ORM object).

    Parameters:
        db(Session): Active SQLAlchemy session used to execute queries on table.
        application(ApplicationCreate): A single job application to a job from a person.
    Returns:
        Application(Application): New job application record.
    """
    # Create new ORM object instance from validated applicant data
    new_application = ApplicationTable(**application.model_dump())

    # Add new application to session and applications table + refresh to ensure ORM object includes all fields
    db.add(new_application)
    db.commit()
    db.refresh(new_application) # updates ORM object to include auto-generated field (e.g., primary key, submitted_date)

    # Convert ORM object into Pydantic Application schema for API response
    return Application.model_validate(new_application)
