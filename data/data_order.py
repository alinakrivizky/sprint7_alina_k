
class OrderData:
    base_order = {
        "firstName": "Monkey",
        "lastName": "D. Luffy",
        "address": "Foosha Village, 14 apt.",
        "metroStation": 4,
        "phone": "+79555345678",
        "rentTime": 4,
        "deliveryDate": "2026-07-01",
        "comment": "If you're hungry, eat!",
    }

    color_cases = [
        ["GREY"],
        ["BLACK"],
        ["BLACK", "GREY"],
        [],
    ]

    color_case_ids = ["grey", "black", "two_colors", "no_color"]
