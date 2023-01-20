import scan_nmap
# em desenvolvimento....


def scan_port(ip, port):
    nm = scan_nmap.PortScanner()
    nm.scan(str(ip), str(port))
    if nm[ip].has_tcp(port):
        state = nm[ip]['tcp'][port]['state']
        print(f'Port {port} on {ip} is {state}')
    else:
        print(f'Port {port} on {ip} is closed or filtered')
