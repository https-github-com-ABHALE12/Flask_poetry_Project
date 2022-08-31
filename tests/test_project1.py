from urllib import response
from project1 import __version__
from app import app
import json

def test_getting():
  response = app.test_client().get('/getting')
  res = json.loads(response.data.decode('utf8')).get("response")
  assert type(res[0]) is list
  assert res[0][0]=='Very bad'
  assert response.status_code ==200



def test_version():
    assert __version__ == '0.1.0'
