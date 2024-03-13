from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import time

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        parsed_path = urllib.parse.urlparse(self.path)
        print("Angeforderter Pfad:", parsed_path.path)
        besserer_pfad = parsed_path.path.replace("/", "")
        self.Zait = time.strftime("%H:%M:%S")
        print("Nummer die angerufen hat/wurde: ", besserer_pfad , "Diese Nummer wurde um ", self.Zait, "Uhr angerufen")
        self.wfile.write(b"<html><head><title>Dings CiM Modul/title></head>")
        self.wfile.write(b"<body><h1>Hier muss garnicht stehen</h1></body></html>")
        threading.Timer(1, self.schließen_browser_tab).start()

    def schließen_browser_tab(self):
        if self.wfile.closed:
            return
        html_response = """
        <script>
            function schließen() {
                window.close();
            }
            window.onload = function() {
                setTimeout(schließen, 1000);
            };
        </script>
        """
        self.wfile.write(html_response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starte nun den Lokalen http Server auf Port: {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
