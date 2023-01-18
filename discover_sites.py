import requests, os

def discover_sites():
    wordlist = input("Enter the wordlist file name: ")
    base_url = input("Enter the base url: ")
    lines = sum(1 for line in open(wordlist))
    html_content = "<html><body>"
    with open(wordlist, 'r') as f:
        for i, line in enumerate(f):
            url = base_url + '/' + line.strip()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print("\033[92m" + f'{url} [+] is accessible - {i+1}/{lines} ({(i+1)/lines*100:.2f}%)' + "\033[0m")
                    html_content += "<p style='color: green'>" + f'{url} is accessible' + "</p>"
            except requests.exceptions.RequestException as e:
                html_content += "<p style='color: red'>" + f'{url} is not accessible' + "</p>"
            print(f'{i+1}/{lines} ({(i+1)/lines*100:.2f}%)', end='\r')
    html_content += "</body></html>"
    with open('result.html', 'w') as f:
        f.write(html_content)
    print()
    input("Press any key to return menu")
    os.system('python main.py') 
