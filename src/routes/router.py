import sys
sys.path.insert(0, '.')
from .user import user_route


class Router(object):
    def __init__(self, object):
        self._r = object
        # self._add_route()
        user_route(self._r)
