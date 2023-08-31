from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRoundFlatButton

from datas.server import Server


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server = Server()

    def on_enter(self):

        login_button = MDRoundFlatButton(text="Login", pos_hint={"center_x":0.5, "center_y":0.4}, on_release=self.login_callback)
        register_button = MDRoundFlatButton(text="Register", pos_hint={"center_x":0.5, "center_y":0.3}, on_release=self.register_callback)

        self.add_widget(login_button)
        self.add_widget(register_button)

        return super().on_enter()
    

    def login_callback(self, item):
        print(self.ids.username.text)
        print(self.ids.password.text)

        cloud_user = self.server.get_user(self.ids.username.text.lower())
        print(cloud_user)

        if cloud_user is None:
            self.ids.log_label.text = "This user was not found. Please register."
            return

        if cloud_user["password"] != self.ids.password.text:
            self.ids.log_label.text = "Incorrect password."
            return

        self.ids.log_label.text = f"Welcome {self.ids.username.text}."

        self.manager.current = "kv_chat_screen"

        print("changed screen")


    def register_callback(self, item):
        print(self.ids.username.text)
        print(self.ids.password.text)

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