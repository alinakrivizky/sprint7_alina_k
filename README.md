# Sprint 7 — Scooter API tests

API-тесты для учебного сервиса `qa-scooter.praktikum-services.ru` на `pytest` + `requests`, с шагами Allure.

## Что покрыто

**Основное задание**
- Создание курьера (`tests/test_create_courier.py`)
- Логин курьера (`tests/test_login.py`)
- Создание заказа (`tests/test_create_order.py`)
- Список заказов (`tests/test_get_orders.py`)

**Дополнительное задание**
- Удаление курьера (`tests/test_delete_courier.py`)
- Принятие заказа (`tests/test_accept_order.py`)
- Получение заказа по номеру (`tests/test_get_order_by_track.py`)

Исходный код тестов — в ветке [`develop`](../../tree/develop).

## Как запустить

```bash
pip install -r requirements.txt  # requests, pytest, allure-pytest
pytest --alluredir=target/allure-results
allure serve target/allure-results
```

## Allure-отчёт

Сырые результаты прогона лежат в `target/allure-results`. Посмотреть отчёт локально:

```bash
allure serve target/allure-results
```
