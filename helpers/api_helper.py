import requests
import urls
from helpers.data_generator import DataGenerate


class ApiHelper:
    @staticmethod
    def create_user():
        payload = DataGenerate.data_generator_for_user()
        response = requests.post(urls.URL_CREATE_USER, data=payload)
        access_token = response.json()['accessToken']
        payload["accessToken"] = access_token
        return payload

    @staticmethod
    def delete_user(payload):
        requests.delete(urls.URL_LOGIN_USER, headers={'Authorization': payload["accessToken"]})
