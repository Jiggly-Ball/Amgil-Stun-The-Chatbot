import json

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivy.core.window import Window
from kivy.utils import platform


from kivymd.app import MDApp

from gui.kivys.app_model import app_kivy
from gui.gui_exec.gui_chat import ChatScreen
from gui.gui_exec.gui_login import LoginScreen

from datas.server import Server


class GuiMain(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open("datas/user_settings.json", "r") as settings_file:
            file_val = json.load(settings_file)
        self.theme = file_val["theme"]
        self.primary_palette = file_val["primary_palette"]

        self.theme_cls.theme_style = self.theme
        self.theme_cls.primary_palette = self.primary_palette

    def on_start(self):

        self.window_manager = ScreenManager(transition=WipeTransition())
        self.window_manager.add_widget(LoginScreen(name="kv_login_screen"))
        self.window_manager.add_widget(ChatScreen(name="kv_chat_screen"))

        return super().on_start()

    def build(self):
        if platform == "android" or platform == "ios":
            Window.maximize()
        else:
            Window.size = (950, 600)

        return Builder.load_string(app_kivy)

App = GuiMain()