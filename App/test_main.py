from main import app

def test_content():
    resp = app.test_client().get('/')
    assert 'Hello' in response.data