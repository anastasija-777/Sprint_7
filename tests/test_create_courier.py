import pytest
import allure
import requests
from methods.create_courier import CreateCourier
from data import URL
from helper import modify_create_courier
from generators import generate_body_create_courier



class TestCreateCourier:

    @allure.step('Проверка, что курьера можно создать, возвращает {"ok":true}')
    def test_successful_create_courier_status_code(self,generate_create_body_courier):
        body = generate_create_body_courier
        response = CreateCourier.create_courier(body)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.step('Проверка, что нельзя создать два одинаковых курьера')
    def test_error_creating_existing_courier(self,generate_create_body_courier):
        body = generate_create_body_courier
        CreateCourier.create_courier(body)
        response = CreateCourier.create_courier(body)
        assert response.status_code == 409

    @allure.step('Проверка, чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize('key',["login","password"])
    def test_error_create_courier_if_one_parameter_absent_status_code(self,key):
        body = generate_body_create_courier()
        payload = modify_create_courier(key, None,body)
        response = requests.post(url=URL.CREATE_COURIER_URL, data=payload)
        result = response.json()
        assert response.status_code == 400
        assert result["message"] == "Недостаточно данных для создания учетной записи"

    @allure.step('Проверка, если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_error_creating_courier_with_existing_login(self,generate_create_body_courier):
        body = generate_create_body_courier
        CreateCourier.create_courier(body)
        payload = modify_create_courier("firstName","saske",body)
        response = requests.post(url=URL.CREATE_COURIER_URL, data=payload)
        assert response.status_code == 409



