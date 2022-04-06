import logging

from starlette_context import context

REQUEST_ID_CTX_KEY = 'X-Request-ID'

def current_request_id():
    """get current request_id inside context var"""
    return context.data[REQUEST_ID_CTX_KEY]


class RequestIDLogFilter(logging.Filter):

    def filter(self, log):
        log.request_id = current_request_id()
        return log
