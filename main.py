from modules.port_scanner import scan_ports
from modules.brute_forcer import brute_force_ssh

def main():
    # Example usage of the port scanner
    ip = "192.168.1.1"
    ports = range(1, 1025)
    open_ports = scan_ports(ip, ports)
    print(f"Open ports on {ip}: {open_ports}")

    # Example usage of the brute forcer
    username = "admin"
    password_list = ["password123", "123456", "admin"]
    brute_force_ssh(ip, username, password_list)

if __name__ == "__main__":
    main()
