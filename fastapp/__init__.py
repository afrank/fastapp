
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import logging
import argparse
import json

class Router(BaseHTTPRequestHandler):
    def do_GET(self):
        for route in routes:
            if self.command not in route.get("methods"):
                continue
            if self.path == route.get("path"):
                pkg = importlib.import_module(route.get("pkg"))
                mod = getattr(pkg,route.get("class"))
                txt = str(mod())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(txt, "utf-8"))
                self.wfile.write(bytes('\n', "utf-8"))
                return

class App:
    def __init__(self,**kwargs):
        logging.basicConfig(format="[%(asctime)s] %(name)s [%(levelname)s]: %(message)s", level=logging.INFO)
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

    def cli(self):
        self.parser = argparse.ArgumentParser(description="cutehttp application server")
        self.parser.add_argument("-b", "--bind", help="Host address to bind to; default 127.0.0.1", default="127.0.0.1")
        self.parser.add_argument("-p", "--port", help="Port to bind to; default 6000", default="6000")

        self.args = parser.parse_args()

