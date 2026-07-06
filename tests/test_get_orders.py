from pages.page_order import OrderPage


class TestGetListOfOrders:
    def test_get_list_of_orders(self):
        order_page = OrderPage()
        response = order_page.get_list_of_orders()
        assert response.status_code == 200
        assert 'orders' in response.json()
