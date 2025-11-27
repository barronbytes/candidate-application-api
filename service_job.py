from sqlalchemy import select
from sqlalchemy.orm import Session
from schema_job import Job
from model_table_job import Job as JobTable


def read_all_jobs(db: Session) -> list[Job]:
    """
    Return all active job openings.

    Parameters:
        db(Session): Active SQLAlchemy session used to query the jobs table.
    Returns:
        list[Job]: Pydantic Job schema objects.
    """
    sql = select(JobTable)  # SELECT * FROM jobs
    jobs = db.execute(sql).scalars().all()
    return [Job.model_validate(job) for job in jobs]