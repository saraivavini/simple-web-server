from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path

class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
    return

  def do_POST(self):
    return

  def do_GET(self):
    self.respond()

  def handle_http(self, status, content_type):
    status = 200
    content_type = "text/plain"
    response_content = ""

    if self.path in routes:
        print(routes[self.path])
        route_content = routes[self.path]['template']
        filepath = Path("templates/{}" .format(route_content))

        if filepath.is_file():
            content_type = "text/html"
            response_content = open("templates/{}".format(route_content))
            response_content = response_content.read()
        else:
            content_type = "text/html"
            response_content = open("templates/error.html")
            response_content = response_content.read()
    else:
        content_type = "text/html"
        response_content = open("templates/error.html")
        response_content = response_content.read()

    self.send_response(status)
    self.send_header('Content - type', content_type)
    self.end_headers()

    return bytes(response_content, "UTF-8")

  def respond(self):
    content = self.handle_http(200, 'text/html')
    self.wfile.write(content)