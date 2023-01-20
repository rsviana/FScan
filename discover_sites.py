import requests, os

def discover_sites():
    wordlist = input("Enter the wordlist file name: ")
    base_url = input("Enter the base url: ")
    lines = sum(1 for line in open(wordlist))
    html_content = "Begin \n\n"
    with open(wordlist, 'r') as f:
        for i, line in enumerate(f):
            url = base_url + '/' + line.strip()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print("\033[92m" + f'{url} [+] is accessible - {i+1}/{lines} ({(i+1)/lines*100:.2f}%)' + "\033[0m")
                    html_content += f'{url} is accessible'
            except requests.exceptions.RequestException as e:
                html_content +=  f'{url} is not accessible' 
            print(f'{i+1}/{lines} ({(i+1)/lines*100:.2f}%)', end='\r')
    html_content += "\n\n------=== EOF ===------"
    with open('result.txt', 'w') as f:
        f.write(html_content)
    print()
    input("Press any key to return menu")
    os.system('python main.py') 
