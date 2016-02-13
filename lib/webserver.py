import cgi
import json
import socket

import http.server
import socketserver
import threading
from devices.base import devices

import settings


request_context = {}


class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            with open("webui/index.html", "r") as index:
                self.send_text_response(index.read())
            return


        if self.path == "/devices":
            result = []
            for device in devices:
                result.append({
                    "name": device.name,
                    "type": device.__class__.__name__,
                    "status": device.get_status()
                })
            #print(result)
            self.send_text_response(result)

        if self.path == "/context":
            self.send_text_response(request_context["context"].serialize())

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        payload = self.rfile.read(content_len)

        command = json.loads(payload.decode("UTF-8"))
       
        try:
           request_context["core"].execute(**command)
           self.send_text_response("ok")
        except Exception as e:
           self.send_text_response("error:%s" % str(e))


    def send_text_response(self, response):

        self.send_response(200)
        self.end_headers()

        if isinstance(response, dict) or isinstance(response, list):
            response = json.dumps(response, indent=3)

        self.wfile.write(bytes(response, 'UTF-8'))

    def log_message(self, format, *args):
        pass


class MyTCPServer(socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


class Webserver(threading.Thread):

    def __init__(self, core, context):

        request_context.update({
            "context": context,
            "core": core
        })

        super(Webserver, self).__init__()
        self.server = MyTCPServer(("", settings.WEBSERVER_PORT), RequestHandler)

    def run(self):
        self.server.serve_forever()
