from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess


PORT = 3000
DOCK_DIR = Path(__file__).resolve().parent / "dock"


def get_tailscale_ip() -> str | None:
    try:
        result = subprocess.run(
            ["tailscale", "ip", "-4"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

    ip = result.stdout.strip().splitlines()
    return ip[0] if ip else None


def main() -> None:
    handler = partial(SimpleHTTPRequestHandler, directory=str(DOCK_DIR))

    server = ThreadingHTTPServer(("0.0.0.0", PORT), handler)
    print(f"Serving {DOCK_DIR} at http://localhost:{PORT}/")
    tailscale_ip = get_tailscale_ip()
    if tailscale_ip:
        print(f"Tailscale access: http://{tailscale_ip}:{PORT}/")
    server.serve_forever()


if __name__ == "__main__":
    main()