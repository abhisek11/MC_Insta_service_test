from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_delete_missing():
    r=client.delete("/images/u1/xxx")
    assert r.status_code==404
