#!/data/data/com.termux/files/usr/bin/python
# HN Designer - Termux Special Edition
# Author: Hasan Nasrullah (sigmaking)
# Project: Sigma Plus Circle - FaceCircle

import os
import time
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear')
    print(Fore.CYAN + Style.BRIGHT + """
  _ _ _ _ ____ _
 | | | | \ | | | _ \ ___ ___(_) __ _ _ __ ___ _ __
 | |_| | \| | | | | |/ _ \/ __| |/ _` | '_ \ / _ \ '__|
 | _ | |\ | | |_| | __/\__ \ | (_| | | | | __/ |
 |_| |_|_| \_| |____/ \___||___/_|\__, |_| |_|\___|_|
                                  |___/
    """)
    print(Fore.YELLOW + Style.BRIGHT + " [ TERMUX EDITION - HN DESIGNER ]")
    print(Fore.WHITE + " Admin: Hasan Nasrullah (sigmaking)")
    print(Fore.GREEN + " Project: T-shart Designe, Totbag Designe, Ad Designe, Socal Mideya Designe, Viral Thumbnail")
    print(Fore.MAGENTA + " ==================================================")

def termux_open(platform, url):
    banner()
    print(Fore.GREEN + Style.BRIGHT + f"\n [+] {platform} Opening...")
    print(Fore.CYAN + "\n [.] Calling Termux Browser...")

    for i in range(3):
        print(Fore.YELLOW + f" Loading{'.' * (i+1)}", end='\r')
        time.sleep(0.5)

    try:
        subprocess.run(["termux-open-url", url])
        print(Fore.GREEN + Style.BRIGHT + f"\n\n [OK] {platform} Opened Successfully!")
    except Exception as e:
        print(Fore.RED + f"\n [X] Error: {e}")
        print(Fore.WHITE + f" Manual Link: {url}")

    input(Fore.CYAN + "\n [ Press Enter to Back to Menu ]")

while True:
    banner()
    print(Fore.WHITE + Style.BRIGHT + "\n [ MAIN MENU - Select Platform ]\n")
    print(Fore.BLUE + Style.BRIGHT + " [01] Facebook - FaceCircle Design")
    print(Fore.MAGENTA + Style.BRIGHT + " [02] TikTok - Viral Thumbnail")
    print(Fore.CYAN + Style.BRIGHT + " [03] Designer Alarm App - Drive Link")
    print(Fore.RED + Style.BRIGHT + " [04] YouTube - Banner & Logo")
    print(Fore.YELLOW + Style.BRIGHT + " [05] Exit Tool")
    print(Fore.CYAN + "\n [Selected platfrom ]")

    choice = input(Fore.GREEN + Style.BRIGHT + "\n HN Designer [~] > ")

    if choice == "1" or choice == "01":
        termux_open("Facebook", "https://www.facebook.com/profile.php?id=61593603822224")
    elif choice == "2" or choice == "02":
        termux_open("TikTok", "https://vm.tiktok.com/ZS9UkrgQ88JvP-kZ3P0/")
    elif choice == "3" or choice == "03":
        drive_link = "https://drive.google.com/file/d/1Xqyo6UYLL0eoFPQruKXa3jZuq1EtAiMZ/view?usp=drivesdk"
        termux_open("Designer Alarm App", drive_link)
    elif choice == "4" or choice == "04":
        termux_open("YouTube", "https://youtube.com/@mdnasrullah-g9j?si=OEh1gAqGMAqC1pbo")
    elif choice == "5" or choice == "05":
        banner()
        print(Fore.GREEN + Style.BRIGHT + "\n [OK] Thanks Bhai! Tool Closing...")
        print(Fore.YELLOW + " Sigmaking Always Rock!")
        time.sleep(1)
        break
    else:
        print(Fore.RED + Style.BRIGHT + "\n [X] Wrong Input! Enter 1-5")
        time.sleep(1)
