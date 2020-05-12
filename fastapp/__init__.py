
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import logging

class Router(BaseHTTPRequestHandler):
    pass

class App:
    def __init__(self,**kwargs):
        self.bind_host = kwargs.get("host", "127.0.0.1")
        self.bind_port = kwargs.get("port", "6000")
        self.router = kwargs.get("router", Router)

        if ':' in self.bind_host:
            self.bind_host,self.bind_port = self.bind_host.split(':')

        self.bind_port = int(self.bind_port)
        self.server = ThreadingHTTPServer((self.bind_host, self.bind_port), self.router)

    def run(self):
        logging.info(f"Starting server on {self.bind_host}:{self.bind_port}, use <Ctrl-C> to stop")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass
        logging.info(f"Stopping server")
        self.server.server_close()

