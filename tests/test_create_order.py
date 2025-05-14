from methods.create_order import CreateOrder
import pytest
import allure

class TestCreateOrder:

    # можно указать один из цветов — BLACK или GREY
    @allure.step('Проверка, что можно указать один из цветов — BLACK или GREY, не указывать или указать два')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY','' ,['BLACK','GREY']])
    def test_create_order_color(self, generate_body_create_order,color):
        body = generate_body_create_order
        response = CreateOrder.create_order(body)
        assert response.status_code == 201

    @allure.step('Проверка, при создании заказа в ответе содержится track')
    def test_create_order_track(self, generate_body_create_order):
        body = generate_body_create_order
        response = CreateOrder.create_order(body)
        assert 'track' in response.text







