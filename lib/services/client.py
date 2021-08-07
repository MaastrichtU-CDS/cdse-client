import json

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from ..core.config import INVOCATION_HOST, SECRET_TOKEN


class Client:
    PREFIX = "http://"
    READY_URL = "/ready"
    RESULT_URL = "/result"

    def get_ready(self):
        try:
            session = requests.session()
            session.headers.update({"Authorization": SECRET_TOKEN.__str__()})
            retry = Retry(total=5, backoff_factor=0.2, status_forcelist=[500])
            session.mount(self.PREFIX, HTTPAdapter(max_retries=retry))
            data = session.get(INVOCATION_HOST + self.READY_URL)
            session.close()
            if len(data.text) > 0:
                return data.json()
            return None
        except ConnectionError as connection_error:
            print(connection_error)

    def post_result(self, results):
        try:
            session = requests.session()
            session.headers = ("Authorization", SECRET_TOKEN)
            retry = Retry(total=5, backoff_factor=0.2, status_forcelist=[500])
            session.mount(self.PREFIX, HTTPAdapter(max_retries=retry))
            session.post(INVOCATION_HOST + self.RESULT_URL, data=json.dumps(results))
            session.close()
        except ConnectionError as connection_error:
            print(connection_error)
