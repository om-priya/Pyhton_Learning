import requests
from functools import lru_cache

from cachetools import cached, TTLCache


class HandleApi:
    def __init__(self, APIID) -> None:
        self.id = APIID
        self.base_url = "https://openexchangerates.org/api/latest.json"

    # will get the rates through api calling
    @property
    # @lru_cache(maxsize=3)
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def rates(self):
        rate = requests.get(f"{self.base_url}?app_id={self.id}").json()
        return rate

    # will convert usd to whatever the rates will return
    def convert_value(self, value):
        rates = self.rates["rates"]["GBP"]
        converted_value = value * rates
        return converted_value
