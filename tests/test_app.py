from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_index() -> None:
    """Home Page Test."""

    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_query_get() -> None:
    """Test get request https://khasguz.hopto.org/docs address."""

    response = client.get('/docs')
    assert response.status_code == 200


def test_fail_query_get() -> None:
    """Test fail get request handler with string parameter."""

    response = client.get(
        '/eval',
        params={'phrase': '(2+2)=2'}
    )
    assert response.status_code == 400
    assert response.text == ('Bad operands or operators')


def test_body_post() -> None:
    """Test post request handler with body parameter."""

    response = client.post(
        '/eval',
        json={'phrase': '(2+2)*2'}
    )
    assert response.status_code == 201
    assert response.json() == {'result': '(2+2)*2 = 8.0'}


def test_fail_body_post() -> None:
    """Test post request handler with body parameter."""

    response = client.post(
        '/eval',
        json={'phrase': '(2+2)=2'}
    )
    assert response.status_code == 400
    assert response.json() == {'error': 'Bad operands or operators'}
