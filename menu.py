from network_scan import network_scan
from discover_sites import discover_sites

def menu():
    print("\033[91m"+"FERRAMENTAS VIANA".center(50, ' ')+"\033[0m")
    print("-"*50)
    print(" "*20 + "1. Scan de rede")
    print(" "*20 + "2. Descobrir sites")
    print(" "*20 + "3. Sair")
    print("-"*50)
    choice = input("Enter your choice: ")
    if choice == "1":
        network_scan()
    elif choice == "2":
        discover_sites()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Try again.")
        menu()