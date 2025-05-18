import requests
from data import URL


class CreateOrder:

    @staticmethod
    def create_order(body):
        payload = body
        response = requests.post(URL.CREATE_ORDER_URL, data=payload)
        return response