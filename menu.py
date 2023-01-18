from network_scan import network_scan
from discover_sites import discover_sites
from getSiteInfo import getSite
import os

def menu():

    width, height = os.get_terminal_size()
    os.system('clear')

    rows, columns = os.popen('stty size', 'r').read().split()
    print()
    print()
    print("="*width)
    center = int(columns) // 2 - len("TOOLS VIANA") // 2
    print(" " *center + "\033[91mTOOLS VIANA\033[0m")
    print("="*width)
    print()
    print(" "*25 + "1. Scan de rede                 5. New Function ")
    print(" "*25 + "2. Descobrir sites              6. New Function")
    print(" "*25 + "3. Resolver DNS                 7. New Function")
    print(" "*25 + "4. New Function                 8. Sair")

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
        exit()
    elif choice == "5":
        exit()
    elif choice == "6":
        exit()                        
    else:
        print("Invalid choice. Try again.")
        menu()