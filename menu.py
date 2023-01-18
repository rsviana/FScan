from network_scan import network_scan
from discover_sites import discover_sites
import os

def menu():

    width, height = os.get_terminal_size()
    os.system('clear')

    rows, columns = os.popen('stty size', 'r').read().split()
    print()
    print()
    print("="*width)
    center = int(columns) // 2 - len("TOOLS VIANA") // 2
    print(" " * center + "\033[91mTOOLS VIANA\033[0m")
    print("="*width)
    print()
    print(" "*center + "1. Scan de rede")
    print(" "*center + "2. Descobrir sites")
    print(" "*center + "3. New Function")
    print(" "*center + "4. New Function")
    print(" "*center + "5. New Function")
    print(" "*center + "6. Sair")    
    print()
    print("="*width)
    choice = input("Enter your choice: ")
    if choice == "1":
        network_scan()
    elif choice == "2":
        discover_sites()
    elif choice == "3":
        exit()
    elif choice == "4":
        exit()
    elif choice == "5":
        exit()
    elif choice == "6":
        exit()                        
    else:
        print("Invalid choice. Try again.")
        menu()