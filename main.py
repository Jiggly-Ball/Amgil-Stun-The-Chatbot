if __name__ == "__main__":

	from model.ai import Ai

	chatbot = Ai(0, 500, 8, "model/intents.json")

	chatbot.train_model()

	while True:
		user_inp = input("You: ")
		response = chatbot.ask_model(user_inp)
		print(f"Bot: {response}")