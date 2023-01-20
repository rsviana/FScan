import nmap,os

def scan_port(ip, port):
    nm = nmap.PortScanner()
    try:
        nm.scan(str(ip), str(port))
        if nm[ip].has_tcp(port):
            state = nm[ip]['tcp'][port]['state']
            print(f'Port {port} on {ip} is {state}')
        else:
            print(f'Port {port} on {ip} is closed or filtered')
    except KeyError:
        print(f'Host {ip} not found')


    print()
    input("Press any key to return menu")
    os.system('python main.py') 
