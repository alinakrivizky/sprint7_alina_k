
import allure
import requests

from data.data_url import Url


class OrderPage:
    BASE_URL = Url.BASE_URL

    def create_order(self, order_data):
        with allure.step("Creating order"):
            return requests.post(f'{self.BASE_URL}/orders', json=order_data)
    def get_list_of_orders(self):
        with allure.step("Getting list of orders"):
            return requests.get(f'{self.BASE_URL}/orders')
    def accept_order(self, order_id, courier_id=None):
        with allure.step("Accepting order"):
            return requests.put(f'{self.BASE_URL}/orders/accept/{order_id}', params={'courierId': courier_id})
    def get_order_by_track(self, track_number=None):
        with allure.step("Getting order by track number"):
            return requests.get(f'{self.BASE_URL}/orders/track', params={'t': track_number})

