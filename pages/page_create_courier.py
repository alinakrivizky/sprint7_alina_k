import requests
import allure

from sprint_7.data.data_url import Url


class PageCreateCourier:
    BASE_URL = Url.BASE_URL

    def create_courier(self, courier_data):
        with allure.step("Creating courier"):
            return requests.post(f'{self.BASE_URL}/courier', data=courier_data)
    def delete_courier(self, courier_id):
        with allure.step("Deleting courier"):
            return requests.delete(f'{self.BASE_URL}/courier/{courier_id}')
