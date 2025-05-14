import requests
import allure
from data import URL


class CreateOrder:

    @allure.step('Получение ответа за запрос - Создать заказ')
    @staticmethod
    def create_order(body):
        payload = body
        response = requests.post(URL.CREATE_ORDER_URL, data=payload)
        return response