# network_scan.py

import socket

def network_scan():
    # Get IP range from user input
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")

    # Ports to scan
    ports = [80, 22]

    # Scanning function
    def port_scanner(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f'Port {port} is open on {ip}')
        else:
            print(f'Port {port} is closed on {ip}')
        sock.close()

    # Get the IP range
    start_ip_parts = start_ip.split(".")
    end_ip_parts = end_ip.split(".")

    # Scanning loop
    for i in range(int(start_ip_parts[3]), int(end_ip_parts[3])+1):
        ip = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
        for port in ports:
            port_scanner(ip, port)
