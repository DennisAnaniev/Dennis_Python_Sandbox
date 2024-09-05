import socket

def scan_ports():
    """
    This function scans a list of ports on a given target host.

    Parameters:
    target_host (str): The IP address or domain name of the target host.

    Returns:
    None. The function prints the status of each port (open or closed) to the console.
    """
    target_host = input("Please enter the IP address or domain name ")
    ports = [22, 80, 443, 10050]
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            is_open = sock.connect_ex((target_host, port)) == 0
            status = "open" if is_open else "closed"
            print(f"Port {port}: {status}")

if __name__ ==  "__main__":
    scan_ports()