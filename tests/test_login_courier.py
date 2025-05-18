from methods.login_courier import LoginCourier
import pytest
import allure


class TestLoginCourier:


    @allure.title('Данный тест проверяет, что курьер может авторизоваться.')
    def test_successful_login_courier(self,generate_create_body_courier):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Создаем курьера и возвращаем список с логином,паролем и именем курьера.'):
            login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        with allure.step('Получаем ответ на запрос авторизоваться.'):
            response = LoginCourier.login_courier(login_pass[0],login_pass[1])
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200


    @allure.title('Данный тест проверяет, что успешный запрос возвращает id.')
    def test_successful_login_courier_return_id(self, generate_create_body_courier):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Создаем курьера и возвращаем список с логином,паролем и именем курьера.'):
            login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        with allure.step('Получаем ответ на запрос авторизоваться.'):
            response = LoginCourier.login_courier(login_pass[0], login_pass[1])
        with allure.step('Проверяем что успешный запрос возвращает id.'):
            assert 'id' in response.text


    @allure.title('Данный тест проверяет, что для авторизации нужно передать все обязательные поля.')
    @pytest.mark.parametrize('login,password', [['anastasija',''],['', '777']])
    def test_error_login_courier_if_password_absent(self, generate_create_body_courier,login,password):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Создаем курьера и возвращаем список с логином,паролем и именем курьера.'):
            login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        with allure.step('Меняем логин на тот который нам нужен.'):
            login_pass[0] = 'anastasija'
        with allure.step('Меняем пароль на тот который нам нужен.'):
            login_pass[1] = '777'
        with allure.step('Получаем ответ на запрос авторизоваться с отсутствующим логином/паролем.'):
            response = LoginCourier.login_courier(login,password)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400
        with allure.step('Проверяем что успешный запрос возвращает "Недостаточно данных для входа".'):
            assert response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Данный тест проверяет, что система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('login,password', [['anastasija', '111'], ['anastas', '777']])
    def test_error_login_courier_if_login_invalid(self,generate_create_body_courier, login,password):
        with allure.step('Генерируем body для запроса "Создание курьера".'):
            body = generate_create_body_courier
        with allure.step('Создаем курьера и возвращаем список с логином,паролем и именем курьера.'):
            login_pass = LoginCourier.register_new_courier_and_return_login_password(body)
        with allure.step('Меняем логин на тот который нам нужен.'):
            login_pass[0] = 'anastasija'
        with allure.step('Меняем пароль на тот который нам нужен.'):
            login_pass[1] = '777'
        with allure.step('Получаем ответ на запрос авторизоваться с неверным логином/паролем.'):
            response = LoginCourier.login_courier(login,password)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404
        with allure.step('Проверяем что успешный запрос возвращает "Учетная запись не найдена".'):
            assert response.json()['message'] == 'Учетная запись не найдена'




