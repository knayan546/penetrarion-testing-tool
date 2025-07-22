# Penetration Testing Toolkit

## Overview
This toolkit provides a modular approach to penetration testing with Python. It includes a port scanner and a brute-forcer module.

## Modules

### Port Scanner
- **Functionality**: Scans specified ports on a given IP address to check if they are open.
- **Usage**:
    ```python
    from modules.port_scanner import scan_ports
    open_ports = scan_ports("192.168.1.1", range(1, 1025))
    ```

### Brute Forcer
- **Functionality**: Attempts to brute force SSH login using a list of passwords.
- **Usage**:
    ```python
    from modules.brute_forcer import brute_force_ssh
    brute_force_ssh("192.168.1.1", "admin", ["password123", "123456"])
    ```

## Requirements
- Python 3.x
- Paramiko library (for SSH brute forcing)

## Installation
1. Clone the repository.
2. Install required libraries:
   ```bash
   pip install paramiko
