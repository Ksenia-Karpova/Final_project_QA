import auxiliary_request
import requests
import data


def test_get_order_positive_assert():
    form_new_order = auxiliary_request.post_new_order(data.order_body)
    get_new_order = auxiliary_request.get_order()
    assert get_new_order.status_code == 200

#Ксения Карпова, 22-я когорта — Финальный проект. Инженер по тестированию плюс