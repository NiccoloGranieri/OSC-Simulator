from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 1337)


for i in range(0, 1000):
    client.send_message("/filter1", [i, i])
    sleep(10)