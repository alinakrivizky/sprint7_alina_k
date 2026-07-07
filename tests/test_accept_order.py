import copy

import allure

from sprint_7.data.data_order import OrderData
from sprint_7.helpers.login_create import Helper
from sprint_7.pages.page_order import OrderPage


class TestAcceptOrder:
    @allure.title("Accepting an order with a valid courier returns 200")
    def test_accept_order(self, page, login_page, courier_cleanup):
        order_page = OrderPage()
        courier_data = Helper.generate_courier_data()
        assert page.create_courier(courier_data).status_code == 201
        login_response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json()["id"]
        courier_cleanup.append(courier_id)
        order_data = copy.deepcopy(OrderData.base_order)
        create_response = order_page.create_order(order_data)
        assert create_response.status_code == 201
        track_number = create_response.json()['track']
        order_id = order_page.get_order_by_track(track_number).json()['order']['id']
        accept_response = order_page.accept_order(order_id, courier_id)
        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}

    @allure.title("Accepting an order without a number returns 404")
    def test_accept_order_without_number(self):
        order_page = OrderPage()
        accept_response = order_page.accept_order("")
        assert accept_response.status_code == 404
        assert accept_response.json() == {"code": 404, "message": "Not Found."}

    @allure.title("Accepting an order without a courier id returns 400")
    def test_accept_without_courier_id(self):
        order_page = OrderPage()
        order_data = copy.deepcopy(OrderData.base_order)
        create_response = order_page.create_order(order_data)
        assert create_response.status_code == 201
        track_number = create_response.json()['track']
        accept_response = order_page.accept_order(track_number, "")
        assert accept_response.status_code == 400
        assert accept_response.json() == {"code": 400, "message": "Недостаточно данных для поиска"}

    @allure.title("Accepting a non-existent order returns 404")
    def test_accept_order_with_nonexistent_id(self, page, login_page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        assert page.create_courier(courier_data).status_code == 201
        login_response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json()["id"]
        courier_cleanup.append(courier_id)
        order_page = OrderPage()
        accept_response = order_page.accept_order(999999, courier_id)
        assert accept_response.status_code == 404
        assert accept_response.json() == {"code": 404, "message": "Заказа с таким id не существует"}

    @allure.title("Accepting an order with a non-existent courier id returns 404")
    def test_accept_order_with_courier_with_nonexistent_id(self):
        order_page = OrderPage()
        order_data = copy.deepcopy(OrderData.base_order)
        create_response = order_page.create_order(order_data)
        assert create_response.status_code == 201
        track_number = create_response.json()['track']
        accept_response = order_page.accept_order(track_number, 999999)
        assert accept_response.status_code == 404
        assert accept_response.json() == {"code": 404, "message": "Курьера с таким id не существует"}
