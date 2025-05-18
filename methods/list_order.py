import requests
from data import URL

class ListOrder:

    @staticmethod
    def list_order(track):
        params = {'t': track}
        response = requests.get(URL.LIST_ORDER_URL,params = params)
        return  response
