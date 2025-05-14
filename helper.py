
import allure



@allure.step('Метод меняет значения ключа при запросе Создать курьера')
def modify_create_courier(key,value,body):
    body_create_courier = body
    body_create_courier [key] =value
    return body_create_courier

@allure.step('Метод меняет значения ключа при запросе Создать заказ')
def modify_create_order(key,value,body):
    body_create_order = body
    body_create_order [key] =value
    return body_create_order


