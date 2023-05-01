import threading
from ReceiverController import ReceiverClient
from SenderController import SenderClient


async def Clients():
    print("Client-Thread1: ")
    thread_1 = threading.Thread(target=ReceiverClient, args=(), daemon=True)
    thread_1.start()
    print("Client-Thread1: ")
    thread_2 = threading.Thread(target=SenderClient, args=(), daemon=True)
    thread_2.start()

