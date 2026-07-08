import allure
import pytest

from helpers.login_create import Helper


class TestCreateCourier:
    @allure.title("Creating a courier with valid data returns 201")
    def test_create_courier(self, page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        courier_cleanup.append({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        response = page.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Creating a courier with an already-used login returns 409")
    def test_create_already_existing_courier(self, page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        courier_cleanup.append({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        page.create_courier(courier_data)
        response = page.create_courier(courier_data)
        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title("Creating a courier with a missing required field returns 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_with_missing_field(self, page, missing_field):
        courier_data = Helper.generate_courier_data()
        del courier_data[missing_field]
        response = page.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
