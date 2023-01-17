import requests

def discover_sites():
    wordlist = "wordlist.txt"
    base_url = input("Enter the base url: ")
    with open(wordlist, 'r') as f:
        for line in f:
            url = base_url + '/' + line.strip()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print("\033[92m" + f'{url} is accessible' + "\033[0m")
            except requests.exceptions.RequestException as e:
                print("\033[91m" + f'{url} is not accessible' + "\033[0m")
    input("Press any key to continue...")

