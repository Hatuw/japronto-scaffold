from config import Config

from japronto import Application

# Load configure
config = Config(debug=True)
config.display()

app = Application()

exit(0)

if __name__ == '__main__':
    app.run(
        debug=config.debug,
        host=config.rest_server_host,
        port=config.rest_server_port
        )
