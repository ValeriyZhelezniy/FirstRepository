import pytest
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_requests():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Responce Body is {r.json()}")
    assert t.status_code == 200
    print(f"Responce Headers are {r.headers}")