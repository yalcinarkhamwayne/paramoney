# ~~~~~~~~~~ ParaMoney ~~~~~~~~~~~~~~~~~
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.label = Label(text="ParaMoney")
        self.add_widget(self.label)
        self.add_widget(Button(text="Neue Einnahme/Ausgabe hinzufügen"))

class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    MyApp().run()
