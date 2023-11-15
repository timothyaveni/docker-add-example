from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class AddRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # Parse query parameters
    parsed_path = urlparse(self.path)
    query_params = parse_qs(parsed_path.query)

    # Extract 'a' and 'b' values and compute the sum
    a = query_params.get('a', [0])[0]
    b = query_params.get('b', [0])[0]
    try:
      sum_result = int(a) + int(b)
      self.send_response(200)
      self.send_header('Content-Type', 'text/plain; charset=utf-8')
      self.end_headers()
      self.wfile.write(f"The sum of {a} and {b} is {sum_result}.".encode())
    except ValueError:
      self.send_error(400, "Invalid input: 'a' and 'b' must be integers.")


httpd = HTTPServer(('0.0.0.0', 3000), AddRequestHandler)
print('Starting httpd server on port 3000')
httpd.serve_forever()
