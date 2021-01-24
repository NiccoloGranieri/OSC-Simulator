from pythonosc.dispatcher import Dispatcher
from typing import List, Any

from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

dispatcher = Dispatcher(0)

def print_handler(address, *args):
    print(f"{address}: {args}")

dispatcher.map("/*", print_handler)  # Map wildcard address to set_filter function

server = BlockingOSCUDPServer(("192.168.1.22", 1339), dispatcher)

server.serve_forever()  # Blocks forever
