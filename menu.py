from network_scan import network_scan
from discover_sites import discover_sites
from getSiteInfo import getSite
from wlist import generate_wordlist
from ssh import ssh_command
from scan_nmap import scan_port
import os, getpass

def menu():

    width, height = os.get_terminal_size()
    os.system('clear')

    rows, columns = os.popen('stty size', 'r').read().split()
    print()
    print()
    print()
    print()
    print("="*width)
    center = int(columns) // 2 - len("TOOLS VIANA") // 2
    print(" " *center + "\033[91mrV ToolS\033[0m")
    print("="*width)
    print()
    print()
    print()
    print()
    print(" "*25 + "1. Network Scan                       5. Client SSH ")
    print(" "*25 + "2. URL Find                           \033[91m6. NMAP\033[0m")
    print(" "*25 + "3. DNS Find                           7. New Function")
    print(" "*25 + "\033[91m4. Wordlist Generator\033[0m" +"                 8. Sair")
    print()
    print()
    print()
    print()
    print("="*width)
    choice = input("Enter your choice: ")
    if choice == "1":
        network_scan()
    elif choice == "2":
        discover_sites()
    elif choice == "3":
        getSite()
    elif choice == "4":
        length = int(input("Enter word length: "))
        num_words = int(input("Enter the number of words: "))
        generate_wordlist(length, num_words)
    elif choice == "5":
        hIp = input("Enter IP Host: ")
        hUser = input("Username host: ")
        hPass = getpass.getpass("Password host: ")
        ssh_command(hIp,hUser,hPass)
    elif choice == "6":
        host = input("Enter the host to scan: ")
        port = input("Enter the port to scan: ")
        result = scan_port(host, port)
        print("The state of port {} on host {} is: {}".format(port, host, result))
    elif choice == "8":
        exit() 
    else:
        print("Invalid choice. Try again.")
        menu()


        

