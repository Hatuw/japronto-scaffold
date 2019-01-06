def hello(request):
    return request.Response(text='Hello {} /!'.format(request.method))

class Router(object):
    def __init__(self, object):
        self._r = object
        self._add_route()

    def _add_route(self):
        self._r.add_route('/', hello)
