if __name__ == "__main__":

	#from model.ai import Ai
#
	#chatbot = Ai(1, 680, 8, "model/intents.json")
#
	##chatbot.train_model()
#
	#while True:
	#	user_inp = input("You: ")
	#	response = chatbot.ask_model(user_inp)
	#	print(f"Bot: {response}")
	import os
	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
	
	from gui.gui_exec.gui_main import App
	from gui.gui_exec.gui_login import LoginScreen
	from kivy.uix.screenmanager import ScreenManager
	from datas.server import Server

	
	
	App.run()

	#window_manager = ScreenManager()
	#window_manager.add_widget(LoginScreen(name="loginscreen"))

	#App = GuiMain()

	#window_manager = ScreenManager()
	#window_manager.add_widget(LoginScreen(name="loginscreen"))

	#App.run()