
import pytest
import allure

class TestCreateOrder:


    @allure.title('Данный тест проверяет, что можно указать один из цветов (BLACK или GREY) либо не указывать либо указать два.')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY','' ,['BLACK','GREY']])
    def test_create_order_color(self, response_create_order, color):
        with allure.step('Получаем ответ на запрос "Создание заказа".'):
            response = response_create_order
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 201


    @allure.title('Данный тест проверяет, что при создании заказа в ответе содержится track')
    def test_create_order_track(self, response_create_order):
        with allure.step('Получаем ответ на запрос "Создание заказа".'):
            response = response_create_order
        with allure.step('Проверяем что успешный запрос возвращает track.'):
           assert 'track' in response.text







