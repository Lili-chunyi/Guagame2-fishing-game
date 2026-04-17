from http.server import *
import threading

def run():
    os.chdir(r"d:\gua game2\fishing")
    server = HTTPServer(('localhost', 8081), SimpleHTTPRequestHandler)
    print("Server running at http://localhost:8081/")
    server.serve_forever()

import os
threading.Thread(target=run, daemon=True).start()
