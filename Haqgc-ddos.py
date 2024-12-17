#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import aiohttp
import asyncio
import colorama
import random
import string 
import time
import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

os.system("clear")
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
faded_text = fade.fire(logo)
print(faded_text)

url = input("\033[92mIP/URL: \033[0m").strip()
url = input("\033[92Press Enter u/ melanjutkan:\033[0m")
                        
async with aiohttp.ClientSession() as session:
     try:
        async with session.get(url) as resp:
            if response.status == 200:
            data = await resp.text()
            <do-stuff-with-data>

urls  = [
         "https://github.com/",
         "https://google.it/",
         "https://facebook.com/",
         "https://alibaba.com/",
         "https://google.com/",
         "https://youtube.com",
         
        ]

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        *(get_cards(url) for url in urls)
        print("[+]>Status Sent")

 else:
                print("Failed ping.")
    except aiohttp.ClientError as e:
                print("\033[92m[+\033[92m] \033[1mAn error occurred:\033[0m", e)

async def main():
    connector = aiohttp.TCPConnector(limit=None) # Enable connection pooling
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(19999):  # Increase the number of concurrent requests
            task = asyncio.create_task(increment_view_count(session))
            tasks.append(task)
            for i in range(19999):  # Increase the number of concurrent requests
                task = asyncio.create_task(increment_view_count(session))
                tasks.append(task)
            await asyncio.gather(*tasks)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
