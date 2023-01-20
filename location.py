import socket,ipinfo,requests,os

def get_location():
    external_ip = requests.get("https://ifconfig.me/ip").text.strip()
    print(external_ip)
    access_token = '85986aa7a82a43'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(external_ip)
    print(f'Localização do host: {details.city}, {details.region}, {details.country}')
    print()
    input("Press any key to return menu")
    os.system('python main.py') 
