import threading
from ReceiverController import ReceiverServer
from SenderController import SenderServer


async def Servers():
    print("Server-Thread1: ")
    thread_1 = threading.Thread(target=ReceiverServer, args=(), daemon=True)
    thread_1.start()
    print("Server-Thread2: ")
    thread_2 = threading.Thread(target=SenderServer, args=(), daemon=True)
    thread_2.start()