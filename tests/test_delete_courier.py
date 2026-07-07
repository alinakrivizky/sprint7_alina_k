import allure


class TestDeleteCourier:
    @allure.title("Deleting an existing courier returns 200")
    def test_delete_courier(self, page, created_courier):
        delete_response = page.delete_courier(created_courier)
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.title("Deleting a courier without an id returns 404")
    def test_delete_courier_without_id(self, page):
        response = page.delete_courier("")
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Not Found."}

    @allure.title("Deleting a non-existent courier returns 404")
    def test_delete_courier_with_nonexistent_id(self, page):
        response = page.delete_courier(999999)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Курьера с таким id нет."}
