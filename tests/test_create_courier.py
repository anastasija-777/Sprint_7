import pytest
import allure
import requests
from methods.create_courier import CreateCourier
from data import URL
from helper import modify_create_courier


class TestCreateCourier:

    @allure.title('Данный тест проверяет успешное создание курьера с правильным статусом ответа.')
    def test_successful_create_courier_status_code(self, response_create_courier):
        with allure.step('Получаем ответ на запрос "Создание курьера".'):
            response = response_create_courier
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 201
        with allure.step('Проверяем что успешный запрос возвращает - "ok":true.'):
            assert response.json() == {"ok": True}


    @allure.title('Данный тест проверяет, что нельзя создать двух одинаковых курьеров.')
    def test_error_creating_existing_courier(self,generate_create_body_courier, response_create_courier):
        with allure.step('Получаем ответ на запрос "Создание курьера".'):
            body = generate_create_body_courier
            response = CreateCourier.create_courier(body)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 409
        with allure.step('Проверяем что успешный запрос возвращает - "Этот логин уже используется".'):
            assert 'Этот логин уже используется' in response.json()['message']


    @allure.title('Данный тест проверяет, что для создания курьера, нужно передать в ручку все обязательные поля.')
    @pytest.mark.parametrize('key',["login","password"])
    def test_error_create_courier_if_one_parameter_absent_status_code(self,generate_create_body_courier,key):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Изменяем значение логина/пароля на пустое.'):
            payload = modify_create_courier(key, '',body)
        with allure.step('Получаем ответ на запрос "Создание курьера" c пустым значением логина/пароля.'):
            response = requests.post(url=URL.CREATE_COURIER_URL, data=payload)
            result = response.json()
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400
        with allure.step('Проверяем что успешный запрос возвращает - "Недостаточно данных для создания учетной записи".'):
            assert result["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Данный тест проверяет, что при создании пользователя с логином, который уже есть, возвращается ошибка.')
    def test_error_creating_courier_with_existing_login(self,generate_create_body_courier,response_create_courier):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Изменяем значение логина/пароля на неправильное.'):
            payload = modify_create_courier("firstName","saske",body)
        with allure.step('Получаем ответ на запрос "Создание курьера" c неправильным значением логина/пароля.'):
            response = requests.post(url=URL.CREATE_COURIER_URL, data=payload)
            result = response.json()
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 409
        with allure.step('Проверяем что успешный запрос возвращает - "Этот логин уже используется".'):
            assert "Этот логин уже используется" in result["message"]


