import requests
import allure
from data import URL


class CreateCourier:

    @allure.step('Получение ответа за запрос - Создать курьера')
    @staticmethod
    def create_courier(body):
        response = requests.post(url=URL.CREATE_COURIER_URL,data=body)
        return response



