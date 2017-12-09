"""
Http Server for application
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

import time

from httphandler import HttpHandler


class HttpServer(object):
    def __init__(self, hostname, port):
        """

        :param hostname:
        :param port:
        """
        self._port = port
        self._handler = HttpHandler
        self._hostname=hostname

    def start(self):
        try:
            self._start_web_server()
        except Exception as ex:
            print()

    def _start_web_server(self):
        self._server = HTTPServer((self._hostname, self._port), self._handler )
        print(time.asctime(), "Server Starts - %s:%s" % (self._hostname, self._port))
        try:
            self._server.serve_forever()
        except KeyboardInterrupt:
            pass