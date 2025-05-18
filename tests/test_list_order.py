from methods.create_order import CreateOrder
from methods.list_order import ListOrder
from data import DataForCreateOrder
import allure


class TestListOrder:


    @allure.title('Данный тест проверяет, что ответ на запрос "Получить заказ по его номеру" показывает список заказа.')
    def test_list_order(self):
        with allure.step('Генерируем body для запроса "Создание заказа".'):
            order = DataForCreateOrder.CREATE_ORDER_BODY
        with allure.step('Получаем ответ на запрос "Создание заказа".'):
            response = CreateOrder.create_order(order)
        with allure.step('В ответе на запрос "Создание заказа" находим track.'):
            track = response.json()['track']
        with allure.step('Получаем ответ на запрос "Получить заказ по его номеру".'):
            list_response = ListOrder.list_order(track)
            result = list_response.json()
        with allure.step('Проверяем код ответа'):
            assert list_response.status_code == 200
        with allure.step('Проверяем что успешный запрос возвращает order.'):
            assert 'order' in result



