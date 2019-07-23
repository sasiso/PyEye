#!/usr/bin/env python3

import argparse
import os
import cv2

import tornado.websocket

parser = argparse.ArgumentParser(description='Start the PyImageStream server.')

parser.add_argument('--port', default=8888, type=int, help='Web server port (default: 8888)')
parser.add_argument('--camera', default=0, type=int, help='Camera index, first camera is 0 (default: 0)')
parser.add_argument('--width', default=640, type=int, help='Width (default: 640)')
parser.add_argument('--height', default=480, type=int, help='Height (default: 480)')
parser.add_argument('--quality', default=70, type=int, help='JPEG Quality 1 (worst) to 100 (best) (default: 70)')
parser.add_argument('--stopdelay', default=7, type=int, help='Delay in seconds before the camera will be stopped after '
                                                             'all clients have disconnected (default: 7)')
args = parser.parse_args()

class ImageWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    get_image_func=None

    def check_origin(self, origin):
        # Allow access from every origin
        return True

    def open(self):
        ImageWebSocket.clients.add(self)
        print("WebSocket opened from: " + self.request.remote_ip)


    def on_message(self, message):
        jpeg_bytes = None

        with open("d:\\img.jpg", "rb") as imageFile:
            jpeg_bytes = imageFile.read()
            #jpeg_bytes = bytearray(f)

        self.write_message(jpeg_bytes, binary=True)

    def on_close(self):
        ImageWebSocket.clients.remove(self)
        print("WebSocket closed from: " + self.request.remote_ip)
        if len(ImageWebSocket.clients) == 0:
            pass


def start_stream_server():
    script_path = os.path.dirname(os.path.realpath(__file__))
    static_path = script_path + '/static/'

    app = tornado.web.Application([
            (r"/websocket", ImageWebSocket),
            (r"/(.*)", tornado.web.StaticFileHandler, {'path': static_path, 'default_filename': 'index.html'}),
        ])
    app.listen(args.port)

    print("Starting server: http://localhost:" + str(args.port) + "/")

    tornado.ioloop.IOLoop.current().start()
