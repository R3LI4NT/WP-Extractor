#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os,sys

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'


os.system("clear")

def banner():
	print("""
\033[1;34m __        ______  \033[1;37m     _______  _______ ____      _    ____ _____ ___  ____  
\033[1;34m \ \      / /  _ \ \033[1;37m    | ____\ \/ /_   _|  _ \    / \  / ___|_   _/ _ \|  _ \ 
\033[1;34m  \ \ /\ / /| |_) |\033[1;37m____|  _|  \  /  | | | |_) |  / _ \| |     | || | | | |_) |
\033[1;34m   \ V  V / |  __/\033[1;37m_____| |___ /  \  | | |  _ <  / ___ \ |___  | || |_| |  _ < 
\033[1;34m    \_/\_/  |_|   \033[1;37m     |_____/_/\_\ |_| |_| \_\/_/   \_\____| |_| \___/|_| \_\  
			   
			 \033[1;41;37m.:.:SIMPLE WORDPRESS EXTRACTOR:.:.\033[0m
			   	    \033[1;44;37m.:R3LI4NT:.\033[0m
""")


def menu():
	print("""
 \033[1;34m[1]\033[0m Scan all Users       \033[1;34m[2]\033[0m Scan all Themes      \033[1;34m[3]\033[0m Scan all Plugins

 \033[1;34m[4]\033[0m WordPress Version    \033[1;34m[5]\033[0m Download joomla + version

""")
