import requests
import allure

from data.data_url import Url


class LoginPage:
    BASE_URL = Url.BASE_URL

    def login(self, credentials):
        with allure.step("Logging in"):
            return requests.post(f'{self.BASE_URL}/courier/login', data=credentials)
