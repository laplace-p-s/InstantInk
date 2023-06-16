import argparse
import http.server
import socketserver
import os
from urllib.parse import parse_qs, urlparse

try:
    APP_NAME = "InstantInk"  # Application Name
    APP_VERSION = "1.0.0"  # Application Version
    
    # Parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="Path to the text file you'd like to edit.")
    args = parser.parse_args()

    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/":
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                with open('editor.html', 'r') as file:
                    self.wfile.write(file.read().encode())
            elif parsed_path.path == "/file.txt":
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open(args.filepath, 'r') as file:
                    self.wfile.write(file.read().encode())
            elif parsed_path.path == "/fileinfo":
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(args.filepath.encode())
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode())
            text = data.get('text', [''])[0]
            with open(args.filepath, 'w') as file:
                file.write(text)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Saved")

    # Starting the server
    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        print(f"{APP_NAME} Ver.{APP_VERSION}")
        print("Serving at: http://localhost:8000")
        httpd.serve_forever()
except Exception as e:
    print(f"An error occurred: {e}")
