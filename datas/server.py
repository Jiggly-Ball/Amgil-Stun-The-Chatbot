import pickle
import dns

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from base64 import b64decode

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=["8.8.8.8"]

with open("datas/token.bin", "rb") as f:
    client = MongoClient(b64decode(pickle.load(f)).decode())
print("Connected to DB")

database = client["ChatDB"]

class Server:
	def __init__(self) -> None:
		self.user_data = database["Users"]
		self.chat_history = database["ChatHistory"]
	
	def get_user(self, username:str) -> (dict | None):
		return self.user_data.find_one({"_id":username})

	def get_all_users(self) -> list:
		return [user["_id"] for user in self.user_data.find({})]
	
	def post_user(self, username:str, password:str) -> bool:
		try:
			self.user_data.insert_one({"_id":username, "password":password})
		except DuplicateKeyError:
			return False
		try:
			self.chat_history.insert_one({"_id":username, "chat_history":[]})
		except DuplicateKeyError:
			return False
		return True


	def get_chat(self, username:str) -> (dict | None):
		return self.chat_history.find_one({"_id":username})

	def update_chat(self, username:str, message:str) -> bool:
		chat_hist = self.get_chat(username=username)
		if chat_hist is None:
			return False
		chat_hist["chat_history"].append(message)
		self.chat_history.update_one({"_id":username}, {"$set":{"chat_history": chat_hist["chat_history"]}})
		return True