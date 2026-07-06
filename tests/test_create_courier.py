import pytest

from helpers.login_create import Helper


class TestCreateCourier:
    def test_create_courier(self, page, login_page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        response = page.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        login_response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_cleanup.append(login_response.json()["id"])

    def test_create_already_existing_courier(self, page, login_page, courier_cleanup):
        courier_data = Helper.generate_courier_data()
        response1 = page.create_courier(courier_data)
        assert response1.status_code == 201
        assert response1.json() == {"ok": True}
        response2 = page.create_courier(courier_data)
        assert response2.status_code == 409
        assert response2.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        login_response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_cleanup.append(login_response.json()["id"])

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_with_missing_field(self, page, missing_field):
        courier_data = Helper.generate_courier_data()
        del courier_data[missing_field]
        response = page.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
