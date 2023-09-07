import pickle
import json

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.utils import asynckivy

from cloud.server import Server
from local.data import Data


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server = Server()

    def on_enter(self):
        if not Data.internet:
            def offline_handler():
                async def offline_mode():

                    await asynckivy.sleep(2)
                    self.manager.current = "kv_chat_screen"

                asynckivy.start(offline_mode())
            offline_handler()

            
        
        else:
            login_button = MDRoundFlatButton(text="Login", pos_hint={"center_x":0.5, "center_y":0.4}, on_release=self.login_callback)
            register_button = MDRoundFlatButton(text="Register", pos_hint={"center_x":0.5, "center_y":0.3}, on_release=self.register_callback)

            self.add_widget(login_button)
            self.add_widget(register_button)

            return super().on_enter()
    
    def on_leave(self):
        self.manager.get_screen("kv_account_screen").ids.username = Data.username
        self.manager.get_screen("kv_account_screen").ids.password = "*" * len(Data.password)

        print(Data.username, Data.password)

        return super().on_enter()

    def login_callback(self, item):
        print(self.ids.username.text)
        print(self.ids.password.text)

        cloud_user = self.server.get_user(self.ids.username.text.lower())
        #print(cloud_user)

        if cloud_user is None:
            self.ids.log_label.text = "This user was not found. Please register."
            return

        if cloud_user["password"] != self.ids.password.text:
            self.ids.log_label.text = "Incorrect password."
            return

        #print(self.ids.check_box_value.text)

        Data.username = self.ids.username.text.lower().strip()
        Data.password = self.ids.password.text

        if Data.remember:
            with open("local/user_info.bin", "wb") as user_info_file:
                pickle.dump({"username":self.ids.username.text.lower().strip(), "password":self.ids.password.text}, user_info_file)
            
            with open("local/user_settings.json", "r") as read_settings:
                settings = json.load(read_settings)

            with open("local/user_settings.json", "w") as write_settings:
                settings["remember"] = True
                json.dump(settings, write_settings)

            print("saved settings")

        self.ids.username.text = ""
        self.ids.password.text = ""
        self.manager.current = "kv_chat_screen"


    def register_callback(self, item):
        #print(self.ids.username.text)
        #print(self.ids.password.text)

        if len(self.ids.username.text.lower().strip()) < 3:
            self.ids.log_label.text = "Your username should be of atleast 3 characters"
            return

        elif len(self.ids.password.text.strip()) < 4:
            self.ids.log_label.text = "Weak password"
            return

        cloud_user = self.server.get_user(self.ids.username.text.lower())

        if cloud_user is not None:
            self.ids.log_label.text = "A user with this name already exists. Please choose another username."
            return

        self.server.post_user(self.ids.username.text.lower().strip(), self.ids.password.text)

        self.ids.log_label.text = f"Successfully created an account under the username: {self.ids.username.text.lower().strip()}\nPlease relogin."

        self.ids.username.text = self.ids.password.text = ""