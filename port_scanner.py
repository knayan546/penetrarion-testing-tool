import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Scan a single port on the given IP address."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        return port, result == 0

def scan_ports(ip, ports):
    """Scan multiple ports on the given IP address."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
    return open_ports
