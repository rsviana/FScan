import ping3,os

def find_active_ips(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    for i in range(start[3], end[3]+1):
        ip = f"{start[0]}.{start[1]}.{start[2]}.{i}"
        response_time = ping3.ping(ip, timeout=1)
        if response_time:
            print("\033[92m" + f"{ip} is active"+ "\033[0m")
        else:
            print("\033[91m"+f"{ip} is inactive"+"\033[0m")
    
    input("Press any key to return menu")
    os.system('python main.py') 