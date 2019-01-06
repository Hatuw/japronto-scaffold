# import os


class Config(object):
    def __init__(self, debug=False):
        # is_production = os.environ['SERVER_ENV'] == 'production'
        self._config = dict(
            debug               = debug,
            rest_server_host    = 'localhost',
            rest_server_port    = 3000,
            )

    def __getitem__(self, attr):
        return self._config[attr]

    def __getattr__(self, attr):
        return self._config[attr]

    # display config (print)
    def display(self):
        print(self._config)

