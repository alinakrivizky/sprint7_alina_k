import random
import string


class Helper:
    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @classmethod
    def generate_courier_data(cls):
        return {
            "login": cls.generate_random_string(),
            "password": cls.generate_random_string(),
            "firstName": cls.generate_random_string()
        }
