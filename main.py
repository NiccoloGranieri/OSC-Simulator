import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Window(Widget):
    def __init__(self, **args):
        super(Window, self).__init__(**args)
        label = Label(text="Port", color=(1, 0, 0, 1))
        port = TextInput()
        conn_button = Button(text="Connect")
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
        return Window()    


if __name__ == '__main__':
    MyApp().run()
