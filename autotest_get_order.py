import auxiliary_request
import requests
import data
import configuration


def test_get_order_positive_assert():
    # Запрос на создание заказа
    form_new_order = auxiliary_request.post_new_order(data.order_body)
    # Сохранение трека заказа
    track_number = form_new_order.json()["track"]
    # Запрос на получения заказа по треку из пункта выше
    get_new_order = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_number))
    # Проверка, что код ответа равен 200
    assert get_new_order.status_code == 200

#Ксения Карпова, 22-я когорта — Финальный проект. Инженер по тестированию плюс