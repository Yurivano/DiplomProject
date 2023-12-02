# Юрий Иванов, 11-я когорта - Финальный проект. Инженер по тестированию плюс.
import sender_stand_requests
import data


def positive_assert_of_create_order_and_save_track(body):
    order_response = sender_stand_requests.post_new_order(body)
    assert order_response.status_code == 201
    assert order_response.json() != ""


def positive_assert_to_receive_an_order_by_its_number(track):
    order_number_response = sender_stand_requests.get_order_by_number(track)
    assert order_number_response.status_code == 200
    assert order_number_response.json() != ""


def test_create_order():
    positive_assert_of_create_order_and_save_track(data.order_body)


def test_recive_order_info():
    positive_assert_to_receive_an_order_by_its_number(data.order_track)
