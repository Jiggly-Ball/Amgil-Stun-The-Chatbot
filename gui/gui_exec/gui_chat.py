from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.list import OneLineListItem

#from commons.threader import Threader
from datas.server import Server
from model.ai import Ai


	

class ChatScreen(Screen):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.chatbot = Ai(1, 680, 8, "model/intents.json")
		self.server = Server()

	def on_enter(self):

		#send_button = MDRoundFlatButton(text="Send", pos_hint={"center_x":0.8, #"center_y":0.1}, on_release=self.send_chat, width=100, size_hint_x=None)
		#self.add_widget(send_button)

		return super().on_enter()

	def ask_model_thread(self, q: str) -> str:
		return self.chatbot.ask_model(q)

	def send_chat(self):
		self.ids.chat_data.add_widget(
			OneLineListItem(
				text=f"You: {self.ids.text_data.text}"
			)
		)

		#response = Threader(target=self.chatbot.ask_model, args=(self.ids.text_data.text.lower().strip(), ))
		response = self.chatbot.ask_model(self.ids.text_data.text.lower().strip())

		self.ids.text_data.text = ""

		if isinstance(response, str):
			self.ids.chat_data.add_widget(
				OneLineListItem(
					text=f"Bot: {response}"
				)
			)
