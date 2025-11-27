from fastapi import FastAPI
from routes import router as api_router


# Create FastAPI instance and add routes
app = FastAPI()
app.include_router(api_router)


# Root endpoint: welcome message in place to confirm API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Candidate Application API!"}