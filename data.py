class URL:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = BASE_URL+'/api/v1/courier'
    LOGIN_COURIER_URL = BASE_URL +'/api/v1/courier/login'
    CREATE_ORDER_URL = BASE_URL + '/api/v1/orders'
    LIST_ORDER_URL = BASE_URL + '/api/v1/orders/track'
    COUNTERMAND_ORDER_URL = BASE_URL + '/api/v1/orders/cancel'



class Data:
    login_invalid = "ninja"


class DataForCreateOrder:
     CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}