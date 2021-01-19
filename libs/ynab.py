import requests


class YouNeedABudgetGET:
    BASE_URL = "https://api.youneedabudget.com/v1"

    def __init__(self, headers, endpoint):
        self.headers = headers
        self.endpoint = endpoint

    def latest(self):
        return requests.get(f"{self.BASE_URL}{self.endpoint}", headers=self.headers).json()


class YouNeedABudgetPOST:
    BASE_URL = "https://api.youneedabudget.com/v1"

    def __init__(self, headers, endpoint, data):
        self.headers = headers
        self.endpoint = endpoint
        self.data = data

    def latest(self):
        return requests.post(f"{self.BASE_URL}{self.endpoint}", headers=self.headers, data=self.data)
