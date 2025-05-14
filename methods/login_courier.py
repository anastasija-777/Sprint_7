import requests
import allure
from data import URL

class LoginCourier:

    @allure.step('Регистрация нового курьера')
    @staticmethod
    def register_new_courier_and_return_login_password(body):
        body = body
        login = body["login"]
        password = body["password"]
        first_name = body["firstName"]
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(URL.CREATE_COURIER_URL, data=body)
        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        # возвращаем список
        return login_pass

    @allure.step('Авторизация курьера')
    @staticmethod
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(URL.LOGIN_COURIER_URL, json=payload)
        return response