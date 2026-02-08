def test_list():
    r=client.get("/images?user_id=u1")
    assert r.status_code==200
