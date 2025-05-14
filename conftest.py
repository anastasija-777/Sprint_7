import pytest
import allure
import requests
from faker import Faker
from data import URL
from generators import generate_body_create_courier
from methods.login_courier import LoginCourier



@allure.step('Создание курьера')
@pytest.fixture(scope="function")
def generate_create_body_courier():
    body = generate_body_create_courier()
    login = body['login']
    password = body['password']

    yield body
    response =LoginCourier.login_courier(login,password)
    id_courier = response.json()['id']
    requests.delete(f'{URL.BASE_URL}/{id_courier}')



@allure.step('Метод генерирует тело для запроса создание заказа')
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











