# Python3 proxy server to change non 404 status code pages to 404
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import hashlib

hostName = "localhost"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        baseURL = ""
        url = baseURL + self.path
        r = requests.get(url)
        if str(hashlib.sha1(bytes(r.text,"utf-8")).hexdigest()) != "404 Hash":
            print("Downloaded " + self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(r.text,"utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Not Found","utf-8"))



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
