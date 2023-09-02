if __name__ == "__main__":
	from model.ai import Ai

	print("START")

	#Ai(1, 700, 8, "model/intents.json").train_model()
	#print("Done")
	while True:
		a = input().lower()
		ask = Ai(1, 700, 8, "model/intents.json").ask_model(a)
		print(ask)

	#print("START")
	#from base64 import b64encode
	#import pickle

	#with open("local/token.bin", "wb") as f:
	#	pickle.dump(
	#		{"mongo":"bW9uZ29kYitzcnY6Ly90b2FzdGVkd2FpZnUwMDpzdGFpY29kZXgyMDIzQGNsdXN0ZXIwLmV3cWFwZHEubW9uZ29kYi5uZXQvP3JldHJ5V3JpdGVzPXRydWUmdz1tYWpvcml#0eQ==", "openai":b"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"} , f)
	#	print("DONE")
	#
	#exit()

	#import os
	#import json
	#import pickle
	#from kivy.utils import platform

	#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
	#os.environ['DEBUG'] = "True"

	#from cloud.server import Server
	#from local.data import Data


	#server = Server()

	#print("Logging in")

	#with open("local/user_settings.json") as user_settings_file:
	#	user_settings = json.load(user_settings_file)

	#print(user_settings)

	#if user_settings["remember"]:
	#	try:
	#		with open("local/user_info.bin", "rb") as user_info_file:
	#			user_info = pickle.load(user_info_file)

	#		cloud_user = server.get_user(user_info["username"])

	#		if cloud_user["password"] == user_info["password"]:
	#			Data.login_allow = True
	#			Data.username = user_info["username"]
	#			#current = "kv_chat_screen"
	#			#self.ids.username.text = user_info["username"]
	#			#self.ids.password.text = user_info["password"]
	#			print("logged in")
	#	
	#	except FileNotFoundError:
	#		pass

	#if platform == "android" or platform == "ios":
	#	Data.device = "phone"
	#else:
	#	Data.device = "pc"

	#from gui.gui_exec.gui_main import GuiMain	# Needs to be placed here for the autologin system to work

	#GuiMain().run()