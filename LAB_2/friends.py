from base_client import BaseClient

import requests

import json

from exception import RequestError


class GetFriends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    # метод vk api
    method = 'friends.get'
    # GET, POST, ...
    http_method = 'GET'

    def __init__(self, uid):
        super().__init__()
        self.uid = uid

    def get_params(self, params):
        self.params = params
        return params

    def _get_data_f(self, params, method=method, http_method=http_method):
        # params = {'user_id': str(self.user_id),'fields' : 'bdate'}
        response = requests.get(self.generate_url(method), params)
        return self.response_handler(response)

    def get_headers(self):
        return None

    # Обработка ответа от VK API
    def response_handler(self, response):
        ret = None
        try:
            data = json.loads(response.text)
            data = data['response']
        except:
            raise RequestError('Bad request')
        else:
            return data

            # Запуск клиента

    def execute(self):
        return self._get_data_f(
            self.method,
            http_method=self.http_method
        )
