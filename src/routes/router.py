from .user import user_route


class Router(object):
    def __init__(self, object):
        self._r = object
        user_route(self._r)
