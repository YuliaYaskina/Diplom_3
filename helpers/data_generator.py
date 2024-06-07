import random
import string


class DataGenerate:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def data_generator_for_user():
        email = f'{DataGenerate.generate_random_string(10)}@yandex.ru'
        password = DataGenerate.generate_random_string(10)
        name = DataGenerate.generate_random_string(10)
        payload = {"email": email, "password": password, "name": name}
        return payload

    def email_generator():
        email = f'{DataGenerate.generate_random_string(10)}@yandex.ru'
        return email
