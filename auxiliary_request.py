import configuration
import requests
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Получение трек-номера заказа
def get_order_track_number():
    response_for_track = post_new_order(data.order_body)
    track_number = response_for_track.json()["track"]
    return track_number

# Переменная для присоединения трек-номера к URL
tr=str(get_order_track_number())
print("Трек-номер заказа: " + tr)

# Получение заказа по трек-номеру
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + tr)

check=get_order()
print("Данные заказа: " + str(check.json()))
print("Код ответа: " + str(check.status_code))

