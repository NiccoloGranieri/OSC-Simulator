import kivy
import asyncio
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher

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


class ConnectionButton(Button):
    def connect(self, instance):
        print(f"{instance} was pressed")


    def __init__(self, **args):
        super(ConnectionButton, self).__init__(**args)
        self.text = 'connect'
        self.bind(on_press=self.connect)


class Window(Widget):
    def __init__(self, **args):
        super(Window, self).__init__(**args)
        label = Label(text="Port", color=(1, 0, 0, 1))
        port = TextInput()
        # conn_button = Button(text="Connect")
        conn_button = ConnectionButton()
        disc_button = Button(text="Disconnect")
        rec_button = Button(text="Record")
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(port)
        layout.add_widget(conn_button)
        layout.add_widget(disc_button)
        layout.add_widget(rec_button)
        
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        """
        This is the main entry point of the app
        """
        # # --- OSC TEST ---
        # dispatcher = Dispatcher()

        # def print_handler(address, *args):
        #     print(f"{address}: {args}")

        # dispatcher.map("/*", print_handler)  # Map wildcard address to set_filter function

        # server = BlockingOSCUDPServer(("192.168.1.22", 1339), dispatcher)

        # server.serve_forever()  # Blocks forever

        # # --- END OSC TEST ---

        return Window()


def print_handler(address, *args):
    print(f"{address}: {args}")


async def main():
    dispatcher = Dispatcher()
    dispatcher.map("/*", print_handler)  # Map wildcard address to set_filter function
    server = AsyncIOOSCUDPServer(("192.168.1.22", 1339), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()

    await MyApp().async_run(async_lib='asyncio')


if __name__ == '__main__':
    asyncio.run(main())
