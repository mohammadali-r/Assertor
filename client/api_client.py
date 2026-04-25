from dataclasses import dataclass
from utils.logger import logger
import requests


@dataclass
class APIClient:
    base_url: str

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, **kwargs)
        logger.info(f"[REQUEST] GET {url}")
        logger.info(f"[RESPONSE] {response.status_code}")
        return response


    def post(self, endpoint, json=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=json)
        logger.info(f"[REQUEST] POST {self.base_url}{endpoint}")
        logger.info(f"[RESPONSE] {response.status_code}")
        return response
