"""Serve the bundled examples on loopback only. Stop with Ctrl-C."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    print('Open http://127.0.0.1:8765/skills/ then choose a skill/assets/example.html', flush=True)
    with ThreadingHTTPServer(('127.0.0.1', 8765), partial(SimpleHTTPRequestHandler, directory=str(root))) as server:
        server.serve_forever()
