#!/usr/bin/env python
#_*_ coding: utf8 _*_


from banner.banner import * 
import json
import urllib.request
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
from os import path
import requests
from progress.bar import Bar
import wget
from xml.etree.ElementTree import parse


banner()
menu()


def restart():
	option = input("\nBack to the main menu (\033[0;32my\033[0m/\033[0;31mn\033[0m): ")
	if option == "y":
		os.system("python3 wp_extractor.py")

	elif option == "n":
		os.system("clear")
		banner()
		print("\n\033[1;37mGoodbye, Friend!\033[0m")
		exit()	


def Scan_users():
    with urllib.request.urlopen(link + complemento) as url:
        for u in json.loads(url.read()):
            user = u['slug']
            print("\033[1;32mUser Found :\033[0m " + user)    


def Scan_themes():
    agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.3'} 
    link = input("URL: ")
    print("")
    request = requests.get(url=link,headers=agent)
    soup = BeautifulSoup(request.text,'html5lib')

    for link in soup.find_all('link'):
        if '/wp-content/themes' in link.get('href'):
            themes = link.get('href')
            themes = themes.split('/')
            if 'themes' in themes:
                pos = themes.index('themes')
                theme = themes[pos+1]
                print("\033[1;33mTheme in use :\033[0m " + theme)

def Scan_plugins():
	#Pugins by: https://plugins.svn.wordpress.org/

    wordlist = input("Wordlist (\033[0;33mdefault: wordlist.txt\033[0m): ")
    print("")
    if path.exists(wordlist):
        wList = open(wordlist,'r')
        wList = wList.read().split('\n')
        lista = []
        bar = Bar("\033[0;31mWait...\033[0m",max=len(wList))

        for plugin in wList:
            bar.next()
            try:
                p = requests.get(url=url+"/"+plugin)
                if p.status_code == 200:
                    final = url + "/wp-content/plugins/" + plugin
                    lista.append(final.split("/")[-2])
            except:
                print("\n\033[1;31mERROR:\033[0m Access Denied or other error")


        bar.finish()
        for plugin in lista:
         	print("\033[1;31mPlugin Found :\033[0m " + plugin) 	             

    else:
        print("\n\033[1;31mERROR:\033[0m Wordlist Not Found :(")


def WP_version():
    header = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url,headers=header)
    soup = BeautifulSoup(peticion.text,'html5lib')

    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
    print("\n\033[1;36mVersion :\033[0m " + version)


def joomla():
    download = wget.download(url=url + directory)
    file = parse("joomla.xml")
    for element in file.findall('version'):
        version = element.text

    print("\n\033[1;34mVersion:\033[0m",version)   


option = int(input("--> "))

if option == 1:
	try:
		link = input("URL: ")
		print("")
		complemento = "/wp-json/wp/v2/users"
		Scan_users()
		restart()

	except HTTPError as err:
		print("\033[1;31mERROR:\033[0m Not Found :(")
		restart()


elif option == 2:
	try:
		Scan_themes()
		restart()

	except:
		pass
		restart()	


elif option == 3:
	try:
		url = input("URL: ")
		Scan_plugins()
		restart()

	except:
		pass
		restart()			


elif option == 4:
	try:
		url = input("URL: ")
		WP_version()
		restart()

	except:
		pass


elif option == 5:
	try:
		url = str(input("URL: "))
		print("")
		directory = '/administrator/manifests/files/joomla.xml'
		joomla()
		restart()

	except:
		pass					
