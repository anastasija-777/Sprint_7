
from methods.login_courier import LoginCourier
import pytest
import allure
from data import Data

class TestLoginCourier:


    @allure.step('Проверка, курьер может авторизоваться')
    def test_successful_login_courier(self,generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier(login_pass[0],login_pass[1])
        assert response.status_code == 200


    @allure.step('Проверка, что для авторизации нужно передать все обязательные поля (не указан пароль)')
    def test_error_login_courier_if_password_absent(self,generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier(login_pass[0],'')
        assert response.status_code == 400

    @allure.step('Проверка, что для авторизации нужно передать все обязательные поля (не указан логин)')
    def test_error_login_courier_if_login_absent(self, generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier('', login_pass[1])
        assert response.status_code == 400


    @allure.step('Проверка, что система вернёт ошибку, если неправильно указать логин')
    def test_error_login_courier_if_login_invalid(self,generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier(Data.login_invalid, login_pass[1])
        assert response.status_code == 404

    @allure.step('Проверка, что система вернёт ошибку, если неправильно указать пароль')
    def test_error_login_courier_if_password_invalid(self,generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier(Data.login_invalid, login_pass[1])
        assert response.status_code == 404


    @allure.step('Проверка, что успешный запрос возвращает id')
    def test_successful_login_courier_return_id(self,generate_create_body_courier):
        body = generate_create_body_courier
        login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        response = LoginCourier.login_courier(login_pass[0],login_pass[1])
        assert 'id' in response.text
