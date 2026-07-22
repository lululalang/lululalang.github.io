#!/usr/bin/env python3
"""
Kimlang Than Portfolio — Local Preview & Test Server
Run this file to preview and test your portfolio site locally before pushing to Git.

Usage:
    python3 server.py
"""

import http.server
import socketserver
import webbrowser
import sys
import os
import time

DEFAULT_PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers for caching prevention during local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def start_server():
    # Ensure working directory is set to this file's folder
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    port = DEFAULT_PORT
    httpd = None
    
    # Find an available port starting from 8000
    for try_port in range(DEFAULT_PORT, DEFAULT_PORT + 20):
        try:
            httpd = socketserver.TCPServer(("", try_port), CustomHTTPRequestHandler)
            port = try_port
            break
        except OSError:
            continue

    if not httpd:
        print("❌ Error: Could not find an open port between 8000 and 8020.")
        sys.exit(1)

    url = f"http://localhost:{port}"
    
    print("\n" + "=" * 62)
    print(" 🔥  Kimlang Than Portfolio — Local Test Server Started! 🔥 ")
    print("=" * 62)
    print(f" ✨  Local Preview URL : {url}")
    print(f" 📁  Serving Directory : {project_dir}")
    print(" 🍷  Opening browser automatically...")
    print(" 🛑  Press Ctrl+C in your terminal to stop the server.")
    print("=" * 62 + "\n")

    # Automatically open default web browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"⚠️  Could not launch browser automatically: {e}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped cleanly by user. Bye! ✨\n")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
