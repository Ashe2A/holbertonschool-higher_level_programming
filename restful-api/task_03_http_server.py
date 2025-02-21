#!/usr/bin/python3
"""
Starting an HTTP server
"""
import http.server
import json


class MyServer(http.server.BaseHTTPRequestHandler):
    """
    My server inherits from
    """
    def do_GET(self):
        """
        Response of the GET request.
        """
        if self.path == "/":
            self.send_response_datatype(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response_datatype(200, json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
                }), "application/json")
        elif self.path == "/status":
            self.send_response_datatype(200, "OK")
        elif self.path == "/info":
            self.send_response_datatype(200, json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
                }), "application/json")
        else:
            self.send_response_datatype(404, "Endpoint not found")

    def send_response_datatype(self, code, message="", datatype="text/html"):
        """
        Send a request response and ensures the datatype of response.
        """
        self.log_request(code)
        self.send_response_only(code, message)
        self.send_header("Content-type", datatype)
        self.end_headers()
        self.wfile.write(message.encode())


def run(server_class=http.server.HTTPServer,
        handler_class=MyServer):
    """
    Running my local server on port 8000
    """
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
