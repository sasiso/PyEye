"""
Application
"""
import httpserver


class Application(object):
    def __init__(self):
        self._port = 8000
        self._hostname = "localhost"
        self._server = None

    def start(self):
        try:
            self._server = httpserver.HttpServer(hostname=self._hostname,
                                                 port=self._port)
            self._server.start()
        except Exception as ex:
            print(ex)
