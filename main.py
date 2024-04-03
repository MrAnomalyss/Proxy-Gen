import requests
import os
import fake_headers 
from fake_headers import Headers
import time
import colorama
from colorama import Fore
import pystyle


print(f""" {Fore.CYAN} 
\n                                                                         
\n     _____        _____           _____                     _____      _____ 
 ___|\    \   ___|\    \     ____|\    \   _____      _____|\    \    /    /|
|    |\    \ |    |\    \   /     /\    \  \    \    /    /| \    \  /    / |
|    | |    ||    | |    | /     /  \    \  \    \  /    / |  \____\/    /  /
|    |/____/||    |/____/ |     |    |    |  \____\/____/   \ |    /    /  / 
|    ||    |||    |\    \ |     |    |    |  /    /\    \    \|___/    /  /  
|    ||____|/|    | |    ||\     \  /    /| /    /  \    \       /    /  /   
|____|       |____| |____|| \_____\/____/ |/____/ /\ \____\     /____/  /    
|    |       |    | |    | \ |    ||    | /|    |/  \|    |    |`    | /     
|____|       |____| |____|  \|____||____|/ |____|    |____|    |_____|/      
  \(           \(     )/       \(    )/      \(        )/         )/         
   '            '     '         '    '        '        '          '          
                                                                             
""")












archivo = 'results.txt'


url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text'




headers = Headers(headers=True).generate()


def proxies_gen():
    response = requests.get(url, headers=headers)
    print(f"{Fore.BLUE}[@] Getting proxies...")
    time.sleep(5)

    if response.status_code == 200:
        with open(archivo , 'w') as f:
            f.write(response.text)
            print(f"{Fore.GREEN}[+]Proxies saved in Results.txt")
            print(f"{Fore.MAGENTA}Wait 5 minutes seconds for new proxies")


while True:
    proxies_gen()
    time.sleep(300)





                





