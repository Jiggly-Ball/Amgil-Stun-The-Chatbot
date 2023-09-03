import json
import pickle

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, WipeTransition

from kivymd.app import MDApp
#from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.menu.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel

from gui.kivys.app_model import app_kivy
from gui.gui_exec.gui_account import AccountScreen
from gui.gui_exec.gui_chat import ChatScreen
from gui.gui_exec.gui_login import LoginScreen
from gui.gui_exec.gui_settings import SettingsScreen

from local.data import Data
from cloud.server import Server


class Stun_Amgil(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open("local/user_settings.json", "r") as settings_file:
            file_val = json.load(settings_file)

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8

        self.theme_cls.theme_style = file_val["theme"]
        self.theme_cls.primary_palette = file_val["primary_palette"]

        self.username = Data.username
        self.password = Data.password
        self.server = Server()
        self.window_manager = ScreenManager(transition=WipeTransition())

    def theme_menu(self, item):

        menu_items = [
            {
                "viewclass":"OneLineListItem",
                "text": "Dark",
                "on_release": lambda x="Dark": self.theme_update(x),
            },

            {
                "viewclass":"OneLineListItem",
                "text": "Light",
                "on_release": lambda x="Light": self.theme_update(x),
            }
        ]

        MDDropdownMenu(
            caller = self.window_manager.get_screen("kv_settings_screen").ids.theme_button, items = menu_items, width_mult = 3, ver_growth="up", hor_growth="right"
        ).open()

    def theme_update(self, theme_name):
        self.theme_cls.theme_style = theme_name

        with open("local/user_settings.json", "r" ) as user_settings_file:
            settings = json.load(user_settings_file)
        
        if settings["theme"] != theme_name:
            settings["theme"] = theme_name
            
            self.window_manager.get_screen("kv_settings_screen").add_widget(MDLabel(text="Restart required.", pos_hint={"center_x": 0.5, "center_y": 0.5})) #ids.setting_log.text = "Restart Required"
            
            with open("local/user_settings.json", "w" ) as user_settings_file:
                json.dump(settings, user_settings_file)


    def primary_palette_menu(self, item):
        menu_items = [
            {
                "viewclass":"OneLineListItem",
                "text": colour,
                "on_release": lambda x=colour: self.primary_palette_update(x),
            } for colour in ["Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue", "LightBlue", "Cyan", "Teal", "Green", "LightGreen", "Lime", "Yellow", "Amber", "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"]
        ]

        MDDropdownMenu(
            caller = self.window_manager.get_screen("kv_settings_screen").ids.primary_palette_button, items = menu_items, width_mult = 3, ver_growth="up", hor_growth="right"
        ).open()
    
    def primary_palette_update(self, palette_name):
        self.theme_cls.primary_palette = palette_name

        with open("local/user_settings.json", "r" ) as user_settings_file:
            settings = json.load(user_settings_file)
        
        if settings["primary_palette"] != palette_name:
            settings["primary_palette"] = palette_name
            
            self.window_manager.get_screen("kv_settings_screen").add_widget(MDLabel(text="Restart required.", pos_hint={"center_x": 0.5, "center_y": 0.5}))
            
            with open("local/user_settings.json", "w" ) as user_settings_file:
                json.dump(settings, user_settings_file)
            
            
    def check(self, checkbox, active):
        print(active)
        Data.remember = active

    def on_start(self):
        self.window_manager.add_widget(ChatScreen(name="kv_chat_screen"))
        self.window_manager.add_widget(LoginScreen(name="kv_login_screen"))
        self.window_manager.add_widget(SettingsScreen(name="kv_settings_screen"))
        self.window_manager.add_widget(AccountScreen(name="kv_account_screen"))
        return super().on_start()

    def refresh_callback(self, *args):
        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def build(self):            
        Data.loaded = True
        return Builder.load_string(app_kivy)