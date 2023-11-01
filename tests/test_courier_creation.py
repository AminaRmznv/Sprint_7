import allure
import requests
import random
import string
from config import API_URL_COURIER_CREATION


@allure.title("Регистрация курьера с корректными данными")
@allure.description("Проверка успешной регистрации курьера с корректными данными")
def test_courier_creation_valid_data_success():
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
    response = requests.post(API_URL_COURIER_CREATION, data=payload)
    courier_id = response.json().get("id")
    print(courier_id)
    print(courier_id)
    assert response.status_code == 201
    assert response.json() == {"ok": True}

@allure.title("Попытка создать курьера без обязательных полей")
@allure.description("Проверка возвращения ошибки при создании курьера без обязательных полей")
def test_courier_creation_without_required_field_returns_error():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "password": password,
        "firstName": first_name
    }
    response = requests.post(API_URL_COURIER_CREATION, data=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

@allure.title("Попытка создать курьера с дублирующимися данными")
@allure.description("Проверка возвращения ошибки при создании курьера с дублирующимися данными")
def test_courier_creation_duplicate_returns_error(new_courier):
    login, password, first_name = new_courier
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(API_URL_COURIER_CREATION, data=payload)
    assert response.status_code == 409
    assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
