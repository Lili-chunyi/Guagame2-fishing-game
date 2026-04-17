import http.server
import socketserver
import os

os.chdir(r"d:\gua game2\fishing")
PORT = 8081

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

Handler = http.server.SimpleHTTPRequestHandler
with ReusableTCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    httpd.serve_forever()
