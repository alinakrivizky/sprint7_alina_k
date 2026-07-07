import allure

from pages.page_order import OrderPage


class TestGetOrderByTrack:
    @allure.title("Getting an order by its track number returns the order")
    def test_get_order_by_track(self, page_order, created_order_track):
        response = page_order.get_order_by_track(created_order_track)
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title("Getting an order without a track number returns 400")
    def test_get_order_by_track_without_track_number(self):
        order_page = OrderPage()
        response = order_page.get_order_by_track()
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для поиска"}

    @allure.title("Getting an order with a non-existent track number returns 404")
    def test_get_order_by_track_with_nonexistent_track_number(self):
        order_page = OrderPage()
        response = order_page.get_order_by_track(999999)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Заказ не найден"}
