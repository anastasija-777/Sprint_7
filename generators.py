import random
import string
import allure



@allure.step('Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Метод генерирует тело для запроса создание курьера')
def generate_body_create_courier():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

