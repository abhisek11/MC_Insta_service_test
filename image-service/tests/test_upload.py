from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_upload():
    r=client.post("/images",
        data={"user_id":"u1"},
        files={"file":("a.jpg",b"abc")}
    )
    assert r.status_code==200
