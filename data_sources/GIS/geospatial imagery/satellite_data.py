import os
import sys
import time
import logging
import requests
import threading

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.handlers.RotatingFileHandler('mptest.log', 'a', 300, 10)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


class RestApi:
    ''' This class enables API requests through managing the frequency,
    and providing event triggers for stream processing or a flag for batch processing systems.

    @author Supratik Chatterjee
    '''

    def __init__(self, name='Random', api_url=None, api_method='GET', daily_max_requests=10000, endpoints=None, store=None):
        '''

        Special note : endpoints are to contain, a list of <endpoint_url> : {method : 'If method different from API method required'. requires_key : 'If API is not required, the URL is executed once daily', delay : 'custom delay'}
        '''
        self.name = name
        self.max_requests = daily_max_requests
        self.url = api_url
        # Useful when API contains multiple endpoints, with the same max_requests count
        self.endpoints = endpoints
        self.count = 0
        self.last_request = None
        self.last_endpoint = None  # used only if endpoints is not None
        self.has_new = False
        if store is None:
            store = os.path.join('apidata', name)
        self.event_hooks = list()
        self.lock = False

    def add_event(self, func):
        while self.lock:
            time.sleep(0.1)
        self.event_hooks.append(func)

    def __process(self, interval):
        while True:
            self.lock = True

            time.sleep(interval)  # seconds

    def start(self):
        # Interval in seconds for making requests
        interval = 24 * 60 * 60 / self.daily_max_requests
        self.__process(interval)


class ApiManager:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._apis = {}
        self._api_count = 0

    def add(self, name: str, api: RestApi):
        if self.capacity is not None:
            if self._api_count >= self.capacity:
                raise Exception('API limit reached')
            if name in self._apis.keys():
                raise Exception('API ID must be unique')
            self._apis[name] = api
            self._api_count += 1

    def remove(self, name):
        if name in self._apis.keys():
            self._apis.pop(name)
            self._api_count -= 1
        else:
            logger.warn()


if __name__ == '__main__':
    api_man = ApiManager('test-manager')
    api = RestApi(name='spectator-free',
                  api_url='api.spectator.earth', api_method="GET", )
    api.create_new()
