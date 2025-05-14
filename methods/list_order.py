import requests
import allure
from data import URL

class ListOrder:

    @allure.step('Получение списка заказа по номеру')
    @staticmethod
    def list_order(track):
        params = {'t': track}
        response = requests.get(URL.LIST_ORDER_URL,params = params)
        return  response
