from sqlalchemy import select
from sqlalchemy.orm import Session
from schema_job import Job
from model_table_job import Job as JobTable


def read_all_jobs(db: Session) -> list[Job]:
    """
    Queries the entire job table (SQLAlchemy ORM objects) and returns a list of
    all active job postings (Pydantic Job schema objects).

    Parameters:
        db(Session): Active SQLAlchemy session used to execute queries on table.
    Returns:
        list[Job]: Active job postings.
    """
    sql = select(JobTable)  # SELECT * FROM jobs
    jobs = db.execute(sql).scalars().all()
    return [Job.model_validate(job) for job in jobs]
