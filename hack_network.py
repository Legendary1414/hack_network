import os

question = input("""

1)capture handshake
2)look at a networks
3)create a wordlist
4)crack hash

""")

if question == "1":
    a1 = input("bssid:")
    b1 = input("channel:")
    a = input("save folder:")
    b = input("handshake name:")
    os.system("airmon-ng start wlan0")
    os.system("airodump-ng --bssid "+a1+" --channel "+b1+" wlan0mon")
elif question == "2":
    os.system("airmon-ng start wlan0")
    os.system("airodump-ng wlan0mon")
elif question == "3":
    os.system("git clone https://github.com/Mebus/cupp")
    os.system("cd cupp")
    os.system("clear")
    os.system("cupp.py -i")
elif question == "4":
    c = input("handshake:")
    d = input("wordlist:")
    os.system("aircrack-ng "+c+"-w "+d)
else:
    print("this operation not found!!!")