import requests

ENDPOINT = "https://todo.pixegami.io"


def test_status_code():
    response = requests.get(ENDPOINT).status_code
    assert response == 200
