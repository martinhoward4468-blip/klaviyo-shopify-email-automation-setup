from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_run_setup_failure_without_credentials():
 response = client.post("/run-setup")
 assert response.status_code == 500