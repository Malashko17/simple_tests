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


@allure.feature("Создание пользователя с валидными данными")
def test_create_valid_group():
    headers = {
        'Content-Type': 'application/json'
    }

    data_json = {
        "name": "123",
        "job": "QA"
    }

    data = json.dumps(data_json)

    response = requests.request(
        'POST',
        'https://reqres.in/api/users',
        headers=headers,
        data=data
    ).json()

    assert response['name'] == '123' and response['job'] == 'QA'