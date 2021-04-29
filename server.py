import os
import http.server as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """Extend SimpleHTTPRequestHandler to handle PUT requests"""
    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        
        filename = os.path.basename(self.path)
        file_length = int(self.headers['Content-Length'])

        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))

        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

if __name__ == '__main__':
    server.test(HandlerClass=HTTPRequestHandler)