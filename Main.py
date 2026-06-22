from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(text="مرحباً بك!", font_size=30)
        self.add_widget(self.label)

        button = Button(text="اضغط هنا", font_size=24)
        button.bind(on_press=self.change_text)
        self.add_widget(button)

    def change_text(self, instance):
        self.label.text = "تم الضغط على الزرار!"


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()