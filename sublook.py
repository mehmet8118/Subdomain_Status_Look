# -*- coding: utf-8 -*-
__author__ = 'mehmet şerif paşa'

import random
import socket
import sys
import threading
import time
import colorama

USERAGENT = [agent.strip() for agent in open('useragent.txt')]
SUBDOMAIN = [sub.strip() for sub in open(str(sys.argv[1]))]

zaman = time.time()

def Saved(put):
    file = open("output.txt","a+")
    file.writelines(str(put)+"\n")

say = 0

def Subdomain_Status_Look():
    global say
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((SUBDOMAIN[say], 80))
        sock.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % SUBDOMAIN[say])
        response = sock.recv(4096)
        print(colorama.Fore.GREEN + SUBDOMAIN[say]+ colorama.Style.RESET_ALL)
        print(response)
        print("-"*60)
        
        if int(response.split()[1]) == 200:
            Saved(str(SUBDOMAIN[say]) + " - " + str(response.split()[1]))
        
        if int(response.split()[1]) == 301:
            Saved(str(SUBDOMAIN[say]) + " - " + str(response.split()[1]))
        
        if int(response.split()[1]) == 302:
            Saved(str(SUBDOMAIN[say]) + " - " + str(response.split()[1]))
        
        else:
            pass
        
        # Hangi STATUS KODLARI(200,301,404 vb.) İstiyorsanız ayarlayın.
        
    except:
        print("Connection Error ==> "+ SUBDOMAIN[say])
    say +=1



thread = []
for i in range(len(SUBDOMAIN)):
    th = threading.Thread(target=Subdomain_Status_Look)
    th.daemon = True
    thread.append(th)
    th.start()
    time.sleep(0.1)

for thjoin in thread:
    thjoin.join()

Son_zaman = int(time.time() - int(zaman))
print("\n\nGeçen Zaman: "+ str(Son_zaman))
