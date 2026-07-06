import copy

from data.data_order import OrderData
from pages.page_order import OrderPage


class TestGetOrderByTrack:
    def test_get_order_by_track(self):
        order_page = OrderPage()
        order_data = copy.deepcopy(OrderData.base_order)
        create_response = order_page.create_order(order_data)
        assert create_response.status_code == 201
        track_number = create_response.json()['track']
        response = order_page.get_order_by_track(track_number)
        assert response.status_code == 200
        assert 'order' in response.json()

    def test_get_order_by_track_without_track_number(self):
        order_page = OrderPage()
        response = order_page.get_order_by_track()
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для поиска"}

    def test_get_order_by_track_with_nonexistent_track_number(self):
        order_page = OrderPage()
        response = order_page.get_order_by_track(999999)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Заказ не найден"}
