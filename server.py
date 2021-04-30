import os
import sys
import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length).decode('utf-8')
        fields = urllib.parse.parse_qs(field_data)
        filename, filedata = S.extract_file_details(fields)

        with open(os.path.join(save_folder, filename), "w") as file:
            file.write(filedata)

        self._set_headers()
        self.wfile.write(self._html("POST!"))

    def extract_file_details(fields):
        from os import linesep

        data = fields[' filename'][0]
        filename = data[:data.find(linesep)].replace('"', '')
        filedata = data[data.find(linesep * 2) + len(linesep * 2):]
        filedata = filedata[:filedata.find("--")]
        filedata = filedata[:filedata.rfind(linesep)]
        filedata = filedata.replace("\r", "")

        return filename, filedata


def run(folder, server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    global save_folder 
    save_folder = folder

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run(sys.argv[1])