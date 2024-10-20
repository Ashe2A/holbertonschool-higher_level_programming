#!/usr/bin/python3

"""
HTTP server.
"""

import http.server
import json


class SimpleHTTPServer(http.server.BaseHTTPRequestHandler):
    """
    Simple HTTP server.
    """

    def do_GET(self):
        """
        Send a GET request.
        """

        if self.path == "/data":
            simple_json = \
                {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
            self.send_response_header_write(200, json.dumps(simple_json),
                                            "application/json")
        elif self.path == "/info":
            info_json_dataset = \
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            self.send_response_header_write(200,
                                            json.dumps(info_json_dataset),
                                            "application/json")
        elif self.path == "/status":
            self.send_response_header_write(200, "OK")
        elif self.path == "/":
            self.send_response_header_write(200,
                                            "Hello, this is a simple API!")
        else:
            self.send_response_header_write(404, "Endpoint not found")
            # 404 Not found (error)

    def send_response_header_write(self, status=200, write="",
                                   datatype="text/html"):
        self.send_response(status)  # Send HTTP response
        self.send_header("Content-type", datatype)
        # Text content type (html/JSON)
        self.end_headers()  # End header sending
        self.wfile.write(write.encode())
        # Send back a message (write() expects bytes (b string))
        # encode() turns the json string into bytes


def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPServer):
    """
    Run the server.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
# Actually run the local server
