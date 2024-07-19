from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class DragDropLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        self.text = file_path.decode("utf-8")

class DragDropApp(App):
    def build(self):
        layout = BoxLayout()
        self.label = DragDropLabel(text="Drag a file here")
        layout.add_widget(self.label)
        return layout

if __name__ == '__main__':
    DragDropApp().run()
