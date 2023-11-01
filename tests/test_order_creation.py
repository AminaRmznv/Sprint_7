import allure
import pytest
import json
import requests
from config import API_URL_ORDERS


@allure.title("Создание заказа с различными цветами успешно")
@allure.description(
    "Проверка успешного создания заказа с различными цветами:можно указать один из цветов — BLACK или GREY, можно указать оба цвета. Тело ответа содержит track")
@pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"]])
def test_order_creation_with_various_colors_success(colors):
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": colors
    }
    payload_string = json.dumps(payload)
    response = requests.post(API_URL_ORDERS, data=payload_string)
    assert response.status_code == 201
    assert "track" in response.json()


@allure.title("Создание заказа без указания цвета успешно")
@allure.description("Проверка успешного создания заказа без указания цвета")
def test_order_creation_without_color_success():
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }
    payload_string = json.dumps(payload)
    response = requests.post(API_URL_ORDERS, data=payload_string)
    assert response.status_code == 201
    assert "track" in response.json()
