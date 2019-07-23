"""
Application
"""
from concurrent.futures.thread import ThreadPoolExecutor

import httpserver
from stream_server.stream_server import start_stream_server
import threading

class Application(object):
    def __init__(self):
        self._port = 8000
        self._hostname = "10.1.1.174"
        self._server = None
        self.t = ThreadPoolExecutor(max_workers=1)

    def start(self):
        try:
            self.t.submit(start_stream_server)
            self._server = httpserver.HttpServer(hostname=self._hostname,
                                                 port=self._port)
            self._server.start()

        except Exception as ex:
            print(ex)
