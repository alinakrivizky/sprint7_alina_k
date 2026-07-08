import allure
import pytest

from data.data_login import LoginData
from helpers.login_create import Helper


class TestLogin:
    @allure.title("Logging in with valid credentials returns 200 and a courier id")
    def test_login_with_valid_credentials(self, page, login_page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        courier_cleanup.append({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        page.create_courier(courier_data)
        response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Logging in with a non-existent account returns 404")
    def test_login_with_nonexistent_account_returns_404(self, login_page):
        response = login_page.login({
            "login": Helper.generate_random_string(),
            "password": Helper.generate_random_string()
        })
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title("Logging in with a wrong password returns 404")
    def test_login_with_wrong_password(self, page, login_page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        courier_cleanup.append({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        page.create_courier(courier_data)
        response = login_page.login({
            "login": courier_data["login"],
            "password": "wrong_" + courier_data["password"]
        })
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title("Logging in with a missing required field returns 400")
    @pytest.mark.parametrize("credentials", [
        LoginData.login_data_missing_password,
        LoginData.login_data_missing_login,
    ], ids=["missing_password", "missing_login"])
    def test_login_with_missing_fields(self, login_page, credentials):
        response = login_page.login(credentials)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}
