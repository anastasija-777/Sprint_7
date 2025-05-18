import requests
from data import URL


class CreateCourier:

    @staticmethod
    def create_courier(body):
        response = requests.post(url=URL.CREATE_COURIER_URL,data=body)
        return response



