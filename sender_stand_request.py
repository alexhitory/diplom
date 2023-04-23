import requests

import configuration
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.order_body)


def get_new_order_track():
    new_order_track = post_new_order(data.order_body)
    track = new_order_track.json()["track"]
    return track


def get_new_order_info(track_body):
    track = get_new_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track),
                        json=track_body,
                        headers=data.headers)


def test_check_status_code():
    response = get_new_order_info(data.track_body)
    assert response.status_code == 200
