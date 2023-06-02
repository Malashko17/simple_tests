import requests
import json
import allure


@allure.id("34")
def test_some_request():
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        'GET',
        'https://dog.ceo/api/breeds/image/random',
        headers=headers
    ).json()

    assert response['status'] == 'success'
