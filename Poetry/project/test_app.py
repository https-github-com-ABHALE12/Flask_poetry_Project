# from book_app import app
from pytest_app import app
import json


def test_get_all_books():
    response = app.test_client().get('/pytest')
    res = json.loads(response.data.decode('utf-8')).get("Info")
    assert type(res[0]) is list
    assert res[0][0]== 'Dipti'
    assert response.status_code == 200
    assert type(res) is list