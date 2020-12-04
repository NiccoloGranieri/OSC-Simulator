from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

def record_data(address, *args):
    rec_file.write(f"{address}: {args}" + "\n")

rec_file = open('rec_test.txt', 'w')

disp = Dispatcher()

disp.map("/some/address*", record_data)

rec_file.close()

ip = "192.168.1.22"
port = 1338

server = BlockingOSCUDPServer((ip, port), disp)
server.serve_forever()  # Blocks forever



# from pythonosc.dispatcher import Dispatcher
# from pythonosc.osc_server import BlockingOSCUDPServer

# def print_handler(address, *args):
#     print(f"{address}: {args}")

# def default_handler(address, *args):
#     print(f"DEFAULT {address}: {args}")

# def record_data(address, *args):
#     saved_data = []
#     saved_data.append(f"{address}: {args}")

# dispatcher = Dispatcher()
# dispatcher.map("/something/*", print_handler)
# dispatcher.set_default_handler(record_data)

# with open('rec_test.txt', 'w') as writer:
#     for item in saved_data:
#         writer.write(f"{item}" + "\n")

# ip = "192.168.1.22"
# port = 1338

# server = BlockingOSCUDPServer((ip, port), dispatcher)
# server.serve_forever()  # Blocks forever