import time
import asyncio
import requests
async def fun1():
    print("fun1 start...")
    await asyncio.sleep(5)
    url='https://www.pexels.com/photo/short-fur-white-and-black-cat-sitting-on-window-1540258/'
    r = requests.get(url, allow_redirects=True)
    open('facebook1.ico', 'wb').write(r.content)
    print("fun1 end...")
async def fun2():
    print("fun2 start...")
    url='https://www.pexels.com/photo/unrecognizable-tourist-standing-under-rough-cliff-in-mountains-during-vacation-3791466/'
    r = requests.get(url, allow_redirects=True)
    open('facebook2.ico', 'wb').write(r.content)
    print("fun2 end....")
    
async def fun3():
    print("fun3 start...")
    url='https://www.pexels.com/photo/white-and-grey-kitten-on-brown-and-black-leopard-print-textile-45201/'
    r = requests.get(url, allow_redirects=True)
    open('facebook3.ico', 'wb').write(r.content)
    print("fun3 end.....")

async def main():
    # await fun1()
    # await fun2()
    # await fun3()
     L=await asyncio.gather(fun1(),
                            fun2(),
                            fun3(),)
asyncio.run(main())