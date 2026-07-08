import copy

import pytest

from data.data_order import OrderData
from helpers.login_create import Helper
from pages.page_create_courier import PageCreateCourier
from pages.page_login import LoginPage
from pages.page_order import OrderPage


@pytest.fixture
def page():
    return PageCreateCourier()
@pytest.fixture
def login_page():
    return LoginPage()
@pytest.fixture
def page_order():
    return OrderPage()
@pytest.fixture
def created_order_track(page_order):
    order_data = copy.deepcopy(OrderData.base_order)
    response = page_order.create_order(order_data)
    return response.json()['track']
@pytest.fixture
def courier_cleanup(page, login_page):
    couriers_credentials = []
    yield couriers_credentials
    for credentials in couriers_credentials:
        login_response = login_page.login(credentials)
        courier_id = login_response.json().get("id")
        if courier_id:
            page.delete_courier(courier_id)

@pytest.fixture
def created_courier(page, login_page, courier_cleanup):
    courier_data = Helper.generate_courier_data()
    courier_cleanup.append({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    page.create_courier(courier_data)
    login_response = login_page.login({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    return login_response.json()["id"]

