import pytest
import requests
import random
import string
import urls
import allure


@allure.title("Регистрация нового курьера")
@allure.description("Метод регистрации нового курьера и удаление курьера после теста.")
@pytest.fixture
def create_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(urls.API_URL_COURIER_CREATION, data=payload)
    yield response
    response_login = requests.post(urls.API_URL_LOGIN, data={'login': login, 'password': password})
    id_courier = response_login.json()['id']
    requests.delete(urls.API_URL_DELETE + f'{id_courier}')


@allure.title("Регистрация нового курьера,возврат логина, пароля и имени.")
@allure.description("Метод регистрации нового курьера и возврат логина, пароля и имени. Удаление курьера после теста")
@pytest.fixture
def create_new_courier_and_return_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    requests.post(urls.API_URL_COURIER_CREATION, data=payload)
    yield login, password, first_name
    response_login = requests.post(urls.API_URL_LOGIN, data={'login': login, 'password': password})
    id_courier = response_login.json()['id']
    requests.delete(urls.API_URL_DELETE + f'{id_courier}')
