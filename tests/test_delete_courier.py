from helpers.login_create import Helper


class TestDeleteCourier:
    def test_delete_courier(self, page, login_page):
        courier_data = Helper.generate_courier_data()
        create_response = page.create_courier(courier_data)
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}
        login_response = login_page.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json()["id"]
        delete_response = page.delete_courier(courier_id)
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    def test_delete_courier_without_id(self, page):
        response = page.delete_courier("")
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Not Found."}

    def test_delete_courier_with_nonexistent_id(self, page):
        response = page.delete_courier(999999)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Курьера с таким id нет."}
