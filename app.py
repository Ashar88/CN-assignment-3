from dotenv import load_dotenv
import asyncio
import os
from ServerDriver import Servers
from ClientDriver import Clients
from ProxyServer.Client import client
from ProxyServer.Proxy_Server import run_server, handle_client

load_dotenv()

runnable = asyncio.run



def client_server_run():
    runnable(Servers())
    runnable(Clients())  

def infinite_looping():
    while True:
      pass

def fileOpening(filename):
    return open(str(os.environ[filename]), encoding='UTF-8', mode='w')


def main():
    if not os.path.exists('logs'):
        os.makedirs('logs')
        try:
            ReceiverPKTLog = open(fileOpening('RECEIVER_LOG_FILENAME'))
            SenderPKTLog = open(fileOpening('SENDER_LOG_FILENAME'))
            ReceiverStreamLogger = open(fileOpening('RECEIVER_LOG_LOGGER'))
            SenderStreamLogger = open(fileOpening('SENDER_LOG_LOGGER'))
            Misc = open(fileOpening('MISC'))
            
        finally:
             pass
    client_server_run(); infinite_looping()


def using_proxy_server():
    client()
    run_server()
    handle_client()


if __name__ == '__main__':
    main()
