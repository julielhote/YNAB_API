import requests


class YouNeedABudget:
    BASE_URL = "https://api.youneedabudget.com/v1"

    def __init__(self, headers, endpoint):
        self.headers = headers
        self.endpoint = endpoint

    def latest(self):
        return requests.get(f"{self.BASE_URL}{self.endpoint}", headers=self.headers).json()
