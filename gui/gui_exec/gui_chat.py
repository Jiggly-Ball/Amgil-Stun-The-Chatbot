from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.list import OneLineListItem

from cloud.server import Server
from local.data import Data
from model.ai import Ai

class ChatScreen(Screen):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.chatbot = Ai(1, 700, 8, "model/intents.json")
		self.server = Server()

	def on_enter(self):

		#send_button = MDRoundFlatButton(text="Send", pos_hint={"center_x":0.8, #"center_y":0.1}, on_release=self.send_chat, width=100, size_hint_x=None)
		#self.add_widget(send_button)

		return super().on_enter()


	def send_chat(self):
		if len(self.ids.text_data.text) == 0:
			return
		
		user_response = f"You: {self.ids.text_data.text}"

		self.ids.text_data.text = ""

		self.ids.chat_data.add_widget(
			OneLineListItem(
				text=user_response
			)
		)

		response = self.chatbot.ask_model(self.ids.text_data.text.lower().strip())
		bot_response = f"Bot: {response}"

		self.ids.chat_data.add_widget(
			OneLineListItem(
				text=bot_response
			)
		)

		self.server.update_chat(Data.username, user_response)
		self.server.update_chat(Data.username, bot_response)