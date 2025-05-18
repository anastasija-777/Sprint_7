import pytest
import allure
import requests
from faker import Faker
from data import URL
from generators import generate_body_create_courier
from methods.login_courier import LoginCourier
from methods.create_courier import CreateCourier
from methods.create_order import CreateOrder


@allure.step('Метод генерирует body  для запроса "Создание курьера"  и по завершению теста удаляет все данные созданного курьера.')
@pytest.fixture(scope="function")
def generate_create_body_courier():
    body = generate_body_create_courier()

    yield body
    login = body['login']
    password = body['password']
    response = LoginCourier.login_courier(login, password)
    id_courier = response.json().get('id')
    requests.delete(f'{URL.BASE_URL}/{id_courier}')


@allure.step('Метод получает ответ на запрос "Создание курьера".')
@pytest.fixture(scope="function")
def response_create_courier(generate_create_body_courier):
    body = generate_create_body_courier
    response = CreateCourier.create_courier(body)
    return response


@allure.step('Метод генерирует body для запроса "Создание курьера".')
@pytest.fixture(scope="function")
def generate_body_create_order():
    faker = Faker()
    body = {
         "firstName": faker.first_name(),
         "lastName": faker.last_name(),
         "address": faker.address,
         "metroStation": faker.random_int(min=1, max=9),
         "phone": faker.random_int(min=10000000000, max=99999999999),
         "rentTime": faker.random_int(min=1, max=9),
         "deliveryDate": faker.date_between(start_date="today", end_date='+1d').isoformat(),
         "comment": faker.word(),
         "color": []
     }
    return body


@allure.step('Метод получает ответ на запрос "Создание заказа".')
@pytest.fixture(scope="function")
def response_create_order(generate_body_create_order):
    body = generate_body_create_order
    response = CreateOrder.create_order(body)
    return response









