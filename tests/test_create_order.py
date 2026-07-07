import copy

import allure
import pytest

from data.data_order import OrderData
from pages.page_order import OrderPage


class TestCreateOrder:
    @allure.title("Creating an order with color={color} returns 201")
    @pytest.mark.parametrize("color", OrderData.color_cases, ids=OrderData.color_case_ids)
    def test_create_order(self, color):
        order_data = copy.deepcopy(OrderData.base_order)
        order_data['color'] = color
        order_page = OrderPage()
        response = order_page.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
