from methods.create_order import CreateOrder
from methods.list_order import ListOrder
from data import DataForCreateOrder
import allure


class TestListOrder:

    @allure.step('Проверка, что ответ на запрос Список заказа показывает список заказа')
    def test_list_order(self):
        order = DataForCreateOrder.CREATE_ORDER_BODY
        response = CreateOrder.create_order(order)
        track = response.json()['track']
        list_response = ListOrder.list_order(track)
        result = list_response.json()
        assert 'order' in result


