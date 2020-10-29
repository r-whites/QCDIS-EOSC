from main import app

def test_content():
    response = app.test_client().get('/')
    assert b'Hello' in response.data