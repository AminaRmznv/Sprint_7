import allure
import requests
from config import API_URL_ORDERS


@allure.title("Получение списка заказов успешно")
@allure.description("Проверка успешного получения списка заказов.В тело ответа возвращается список заказов")
def test_recieving_list_of_orders_success():
    response = requests.get(API_URL_ORDERS)
    assert "orders" in response.json()
