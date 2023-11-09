import allure
import requests
from urls import API_URL_ORDERS


class TestCourierCreation:
    @allure.title("Получение списка заказов успешно")
    @allure.description("Проверка успешного получения списка заказов.В тело ответа возвращается список заказов")
    def test_recieving_list_of_orders_success(self):
        response = requests.get(API_URL_ORDERS)
        assert "orders" in response.json()
