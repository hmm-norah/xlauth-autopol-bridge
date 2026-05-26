import os
from http.server import HTTPServer, BaseHTTPRequestHandler

ini = 'retail.ini'

ashita = 'ashita-cli.exe'
ip = '0.0.0.0'
port = 4646


def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    httpd = HTTPServer((ip, port), Serv)
    httpd.serve_forever()

class Serv(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=UTF-8\n' +
        '\n{\"app\":\"XIVLauncher\", \"version\":\"legacy-7.0.20.0\"}')
        self.end_headers()

    def do_GET(self):
       self._set_headers()
       if self.path.startswith('/ffxivlauncher/',):
          otp = self.path[15:21]
          print("Sending otp: " + otp)
          os.system(ashita + ' ' + ini + ' ' + str(otp))
          quit()

if __name__ == "__main__":
    main()