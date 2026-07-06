import pytest

from pages.page_create_courier import PageCreateCourier
from pages.page_login import LoginPage


@pytest.fixture
def page():
    return PageCreateCourier()


@pytest.fixture
def login_page():
    return LoginPage()


@pytest.fixture
def courier_cleanup(page):
    courier_ids = []

    yield courier_ids

    for courier_id in courier_ids:
        page.delete_courier(courier_id)

