import allure
import requests
from config import API_URL_LOGIN


@allure.title("Вход курьера с корректными данными")
@allure.description("Проверка успешного входа курьера с корректными данными.")
def test_login_courier_with_valid_data_success(new_courier):
    login, password, first_name = new_courier
    payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(API_URL_LOGIN, data=payload)
    assert response.status_code == 200
    assert "id" in response.json()


@allure.title("Попытка входа курьера с некорректными данными")
@allure.description("Проверка возвращения ошибки при попытке входа курьера с некорректными данными")
def test_login_courier_with_invalid_data_returns_error(new_courier):
    login, password, first_name = new_courier
    payload = {
        "login": login+"1",
        "password": password+"1"
    }
    response = requests.post(API_URL_LOGIN, data=payload)
    assert response.status_code == 404
    assert response.json()["message"] == "Учетная запись не найдена"


@allure.title("Попытка входа курьера с отсутствующими полями")
@allure.description("Проверка возвращения ошибки при попытке входа курьера с отсутствующими полями")
def test_login_courier_missing_fields_returns_error(new_courier):
    login, password, first_name = new_courier
    payload = {
        "login": login,
        "password": ""
    }
    response = requests.post(API_URL_LOGIN, data=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Недостаточно данных для входа"
