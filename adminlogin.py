import argparse
import requests
from datetime import datetime

site = argparse.ArgumentParser()
site.add_argument("-u", help = "URL adresi örn: https://seninsiten.com/")
site.add_argument("-w", help = "wordlist dosyası örn: wordlist.txt")
args = site.parse_args()
tarih = datetime.now()


print("\033[36m" + """
              _           _        _____                                 
     /\      | |         (_)      / ____|                                
    /  \   __| |_ __ ___  _ _ __ | (___   ___ __ _ _ __  _ __   ___ _ __ 
   / /\ \ / _` | '_ ` _ \| | '_ \ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / ____ \ (_| | | | | | | | | | |____) | (_| (_| | | | | | | |  __/ |   
 /_/    \_\__,_|_| |_| |_|_|_| |_|_____/ \___\__,_|_| |_|_| |_|\___|_| """ + "\033[0m")

print("\033[34m" + "                                             GitHub: Bahahaha-r00t" + "\033[0m")
print("--------------------------------------------------------------------------")
print("\033[35m" + f"[{tarih}]" + "\033[0m")
print("")

url = args.u
wordlist = args.w
default_color = "\033[0m"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
    }
sayac = 0
dosya = open(args.w, "r")
satirlar = dosya.readlines()
dosya.close()
satir_sayisi = len(satirlar)


while sayac < satir_sayisi:
    url2 = url + satirlar[sayac].strip()
    response = requests.get(url2, headers=headers)

    if (response.status_code == 200):
        print("\033[32m" + f"[+] OK - {url2}" + default_color)

    elif (response.status_code == 403):
        print("\033[33m" + f"[-]403 Forbidden - {url2}" + default_color)

    elif (response.status_code == 404):
        print("\033[31m" + f"[-]404 Not Found - {url2}" + default_color)

    else:
        print("\033[31m" + f"[-]500 Internal Server Error - {url2}" + default_color)

    sayac += 1
