import kivy
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher

# # Async Stuff
from multiprocessing import Process

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# OSC Test
from pythonosc.dispatcher import Dispatcher
from typing import List, Any

from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

class MyServer():
    dispatcher = Dispatcher()
    server = None

    def callback(*values):
        print("got values: {}".format(values))

    def start(self, address='192.168.1.13', port=8234, default=True):
        self.dispatcher.map("/accxyz", self.callback)  # Map wildcard address to set_filter function
        self.server = BlockingOSCUDPServer((address, port), self.dispatcher)
        self.server.serve_forever()

    def stop(self, instance):
        # Stop the server. Can you stop it, or do we need to kill it?
        self.server.shutdown()

    def updateListenAddress(self):
        # Update the server_forever address somehow
        pass

class ConnectionButton(Button):
    def connect(self, instance):
        print(f"{instance} was pressed")


    def __init__(self, **args):
        super(ConnectionButton, self).__init__(**args)
        self.text = 'connect'
        self.bind(on_press=self.connect)

class Window(Widget):
    server = MyServer()
    process: Process

    def __init__(self, **args):
        super(Window, self).__init__(**args)
        label = Label(text="Port", color=(1, 0, 0, 1))
        port = TextInput()
        # conn_button = Button(text="Connect")
        conn_button = ConnectionButton()
        disc_button = Button(text="Disconnect", on_press=self.server.stop)
        rec_button = Button(text="Record")
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(port)
        layout.add_widget(conn_button)
        layout.add_widget(disc_button)
        layout.add_widget(rec_button)

        # self.process = Process(target=server.start, args=('127.0.0.1', 8000, True))
        self.process = Process(target=self.server.start)
        self.process.start()

        self.add_widget(layout)

class MyApp(App):
    def build(self):
        """
        This is the main entry point of the app
        """
        return Window()

if __name__ == '__main__':
    MyApp().run()
