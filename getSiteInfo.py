import socket,os
import dns.resolver

def getSite():
    hostname = input("Enter a hostname: ")
    ns_records = dns.resolver.query(hostname, 'NS')
    soa_records = dns.resolver.query(hostname, 'SOA')
    ip_address = socket.gethostbyname(hostname)
    print("IP address of {} is: {} ".format(hostname, ip_address))
    try:
        print("NS records for {}: ".format(hostname))
        for ns in ns_records:
            print(ns.to_text())
            print("SOA records for {}: ".format(hostname))
            print("-"*100)
        for soa in soa_records:
            print(soa.to_text())
            host_info = socket.gethostbyaddr(ip_address)
            print("Hostname: {} ".format(host_info[0]))
            print("-"*100)
            print("Aliases: {} ".format(", ".join(host_info[1])))
            print("-"*100)
            print("Addresses: {} ".format(", ".join(host_info[2])))
            print("-"*100)
    except socket.herror as e:
        print("Error: {}".format(e))

    print()
    input("Press any key to return menu")
    os.system('python main.py') 
