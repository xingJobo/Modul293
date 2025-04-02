from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Parse query parameters from the URL
        query_string = self.path.split('?', 1)[1] if '?' in self.path else ''
        parsed_data = urllib.parse.parse_qs(query_string)
        
        print("Received GET Data:", parsed_data)
        
        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        response = f"<h1>GET Data Received!</h1><p>Data: {parsed_data}</p>"
        self.wfile.write(response.encode("utf-8"))

    # Handle POST requests
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        
        # Parse the POST data
        parsed_data = urllib.parse.parse_qs(post_data)
        
        print("Received POST Data:", parsed_data)
        
        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        response = f"<h1>POST Data Received!</h1><p>Data: {parsed_data}</p>"
        self.wfile.write(response.encode("utf-8"))

# Set up and run the server
server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleRequestHandler)
print("Server running on http://localhost:8000")
httpd.serve_forever()