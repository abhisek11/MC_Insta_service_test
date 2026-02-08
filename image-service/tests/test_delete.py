def test_delete_missing():
    r=client.delete("/images/u1/xxx")
    assert r.status_code==404
