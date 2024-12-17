import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3-pip")
    os.system("pip install requests")
    os.system("pip install asyncio")
    os.system("pip install aiohttp")
    os.system("pip install fade")
elif c == "1":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3-pip")
    os.system("pip3 install requests")
    os.system("pip3 install asyncio")
    os.system("pip3 install aiohttp")
    os.system("pip3 install fade")
print("Done.")
