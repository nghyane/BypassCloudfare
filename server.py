import http.server
import socketserver
import io
import threading
from socket import create_server

from function import bypass
from urllib.parse import parse_qs

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    # Handler for the GET requests

    def do_GET(self):
        try:
            print(self.requestline)
            qs = parse_qs(self.path[2:])

            if 'url' not in qs:
                self.wfile.write('URL not found!'.encode())
                return

            url = (qs['url'][0])

            if 'ref' in qs:
                ref = (qs['ref'][0])
            else:
                ref = url

            res = bypass(url, ref)
            headers = res.headers

            self.send_response(res.status_code)
            self.send_header('Content-type', headers['Content-Type'])
            self.end_headers()

            if "image" in headers['Content-Type']:
                with io.BytesIO(res.content) as file_handle:
                    content = (file_handle.getvalue())
            else:
                content = res.text.encode()

            self.wfile.write(content)
        finally:
            return


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

threading.Thread(target=create_server).start()
