from fastapi import FastAPI
from route_company import router as company_router
from route_applicant import router as applicant_router


app = FastAPI()

# Include routers for user types
app.include_router(company_router)
app.include_router(applicant_router)


# Root endpoint: welcome message in place to confirm API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Candidate Application API!"}