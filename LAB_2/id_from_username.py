from base_client import BaseClient
import requests
import json
from exception import RequestError

class IdFromUsername(BaseClient):
    """Класс для получения id пользователя из username"""

    # URL vk api
    BASE_URL = 'https://api.vk.com/method/'
    # метод vk api
    method = 'users.get'
    # GET, POST, ...
    http_method = 'GET'

    def get_params(self,params):
        self.params = params
        return params

    def _get_data(self, method = method, http_method = http_method):
        response = requests.get(self.generate_url(method),self.params)


        # todo выполнить запрос
        return self.response_handler(response)


    # Обработка ответа от VK API ????
    def response_handler(self, response):
        ret = None
        try:
            data = json.loads(response.text)
            self.uid = data['response'][0]['uid']
            ret = data['response'][0]
        except:
            raise RequestError('Bad request')
        return ret

        # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )












