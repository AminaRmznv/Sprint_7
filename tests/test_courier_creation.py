import allure
import requests
from urls import API_URL_COURIER_CREATION
import urls


class TestCourierCreation:

    @allure.title("Регистрация курьера с корректными данными")
    @allure.description("Проверка успешной регистрации курьера с корректными данными")
    def test_courier_creation_valid_data_success(self, create_new_courier):
        assert create_new_courier.status_code == 201
        assert create_new_courier.json() == {"ok": True}

    @allure.title("Попытка создать курьера без обязательных полей")
    @allure.description("Проверка возвращения ошибки при создании курьера без обязательных полей")
    def test_courier_creation_without_required_field_returns_error(self):
        payload = {
            "password": 'anypassword',
            "firstName": 'anyfirst_name'
        }
        response = requests.post(API_URL_COURIER_CREATION, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Попытка создать курьера с дублирующимися данными")
    @allure.description("Проверка возвращения ошибки при создании курьера с дублирующимися данными")
    def test_courier_creation_duplicate_returns_error(self, create_new_courier_and_return_data):
        login, password, first_name = create_new_courier_and_return_data
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(urls.API_URL_COURIER_CREATION, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
