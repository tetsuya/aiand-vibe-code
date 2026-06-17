#!/usr/bin/env python3
"""
Simple HTTP server for Tetsuya's portfolio site.
Usage:
    python3 deploy.py [port]

Defaults to port 80 if run with sudo/root, otherwise port 8000.
"""
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else (80 if os.geteuid() == 0 else 8000)
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean log formatting
        print(f"[{self.log_date_time_string()}] {args[0]}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("=" * 40)
        print("  Tetsuya Portfolio Server")
        print("=" * 40)
        print(f"Serving: {DIRECTORY}")
        print(f"URL:     http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        print("-" * 40)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
