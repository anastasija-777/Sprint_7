import allure


@allure.step('Метод изменяет значение ключа в словаре body запроса "Создание курьера".')
def modify_create_courier(key,value,body):
    body_create_courier = body
    body_create_courier [key] =value
    return body_create_courier

@allure.step('Метод изменяет значение ключа в словаре body запроса "Создание заказа".')
def modify_create_order(key,value,body):
    body_create_order = body
    body_create_order [key] =value
    return body_create_order


