from config import Config
from routes.router import Router

from japronto import Application

# Load configure
config = Config(debug=True)

# create an app
app = Application()
# add routes
app_rt = app.router
Router(app_rt)

if __name__ == '__main__':
    app.run(
        debug=config.debug,
        host=config.rest_server_host,
        port=config.rest_server_port
        )
