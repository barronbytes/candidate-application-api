# AI-generated test file
import unittest
from fastapi.testclient import TestClient
from main import app
from model_database import Base, engine


client = TestClient(app)


class TestApplicationSubmission(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure table exists before tests run
        Base.metadata.create_all(bind=engine)


    @classmethod
    def tearDownClass(cls):
        # Drop all tables after tests run
        Base.metadata.drop_all(bind=engine)


    def test_create_application_success(self):
        payload = {
            "job_id": 1,
            "candidate_name": "John Doe",
            "email": "johndoe@example.com",
            "resume_file_path": "/resumes/johndoe.pdf",
            "cover_letter": "Excited to apply!"
        }
        response = client.post("/api/applications", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["job_id"], payload["job_id"])
        self.assertEqual(data["candidate_name"], payload["candidate_name"])
        self.assertEqual(data["email"], payload["email"])
        self.assertEqual(data["resume_file_path"], payload["resume_file_path"])


    def test_create_application_missing_name(self):
        payload = {
            "job_id": 1,
            "email": "johndoe@example.com",
            "resume_file_path": "/resumes/johndoe.pdf"
        }
        response = client.post("/api/applications", json=payload)
        # FastAPI/Pydantic should reject this with 422 Unprocessable Entity
        self.assertEqual(response.status_code, 422)


    def test_create_application_invalid_email(self):
        payload = {
            "job_id": 1,
            "candidate_name": "John Doe",
            "email": "not-an-email",
            "resume_file_path": "/resumes/johndoe.pdf"
        }
        response = client.post("/api/applications", json=payload)
        self.assertEqual(response.status_code, 422)


    def test_create_application_missing_resume(self):
        payload = {
            "job_id": 1,
            "candidate_name": "John Doe",
            "email": "johndoe@example.com"
        }
        response = client.post("/api/applications", json=payload)
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
