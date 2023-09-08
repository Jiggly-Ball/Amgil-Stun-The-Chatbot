import nltk
import numpy
import random
import json
import pickle
import tflearn
import tensorflow
import openai

from nltk.stem.lancaster import LancasterStemmer
from typing import Literal

class Ai:
	def __init__(self, model_no:int , n_epochs:int, batch_size:int, dataset:str) -> None: 
		try:
			nltk.data.find("tokenizers/punkt")
		except LookupError:
			nltk.download("punkt")		# This requires the device to be connected to the internet

		self.MODEL_NO   = model_no
		self.N_EPOCHS   = n_epochs   	# Number of times the model will train data from it
		self.BATCH_SIZE = batch_size	# Number of middle neurons

		self.stemmer = LancasterStemmer()
		self.dataset = dataset		# The file location of the dataset over which the AI is going to train over

		self.ignore_chars 				= ("?", "!", ".", ",", "|")	# Characters to be ignored while training
		self.confidence_threshold 		= 0.818						# Requires atleast 81.8% confidence rate on the highest probable result to show the output to the user

		self.classify:	dict | None			 = None
		self.words:		list | None			 = None
		self.labels:	list | None			 = None
		self.training:	numpy.ndarray | None = None
		self.output:	numpy.ndarray | None = None

		#openai.api_key = "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"
		openai.api_key = "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"

	def connect_model(self, training_: numpy.ndarray, output_: numpy.ndarray, mode: Literal["train", "load"]) -> (tflearn.DNN | None):
		"""
		Optimizes and creates / loads a fully connected neural network
		"""

		tensorflow.compat.v1.reset_default_graph()

		net = tflearn.input_data(shape=[None, len(training_[0])])
		net = tflearn.regression(
			tflearn.fully_connected(
				tflearn.fully_connected(
					tflearn.fully_connected(
						net,
					8),
				8),
			len(output_[0]), activation="softmax")	# Softmax gives its neurons probability range based on how accurate it is with it's output
		)

		model = tflearn.DNN(net)

		if (mode := mode.lower().strip()) == "load":
			model.load(rf"model\model_versions\MV{self.MODEL_NO}\generative_model_{self.MODEL_NO}.{self.N_EPOCHS}.{self.BATCH_SIZE}.tflearn")
		
		elif mode == "train":
			model.fit(training_, output_, n_epoch=self.N_EPOCHS, batch_size=self.BATCH_SIZE, show_metric=True)
			model.save(rf"model\model_versions\MV{self.MODEL_NO}\generative_model_{self.MODEL_NO}.{self.N_EPOCHS}.{self.BATCH_SIZE}.tflearn")
		
		else:
			return None

		return model

	
	def ask_model(self, user_input: str) -> str:
		"""
		@user_input: The question you want to ask the pre trained AI
		"""

		try:
			with open(self.dataset, "r") as intents:
				data = json.load(intents)

		except FileNotFoundError:
			return print("ERROR: The intents file doesn't exist for referencing model")
		
		if any(arr is None for arr in (self.words, self.labels, self.training, self.output)): #  Since all the elements are of iterable types we need to manually check weather each elemnt is of None type. 
			with open(rf"model\model_versions\MV{self.MODEL_NO}\train_data\training_data_{self.MODEL_NO}.bin", "rb") as training_data_file:
				self.words, self.labels, self.training, self.output = pickle.load(training_data_file)
			
		if self.classify is None:
			with open(rf"model\model_versions\MV{self.MODEL_NO}\train_data\intents_classify_{self.MODEL_NO}.bin", "rb") as intents_classify_file:
				self.classify = pickle.load(intents_classify_file)
		
		model = self.connect_model(self.training, self.output, "load")

		# Using the bag-of-words method over the user's input to search over the model's trained data
		# Basically converting the user input to a format through which the AI was trained by
		bag = [0 for _ in range(len(self.words))]

		tokenized_words = [self.stemmer.stem(word.lower()) for word in nltk.word_tokenize(user_input)]

		for t in tokenized_words:
			for index, word in enumerate(self.words):
				if word == t:
					bag[index] = 1
		
		prediction_values = model.predict([numpy.array(bag)])[0]
		prediction_result =  numpy.argmax(prediction_values)
		tag_result = self.labels[prediction_result]

		print()
		print(prediction_values)
		print(prediction_values[prediction_result])
		print(tag_result)
		print()

		if (prediction_values[prediction_result] < self.confidence_threshold):
			try:
				print("GPT")
				gpt_prompt = openai.ChatCompletion.create(
					max_tokens=75,
					model="gpt-3.5-turbo",
					messages=[
						{"role": "user", "content": user_input}
						]
					)
				return gpt_prompt["choices"][0]["message"]["content"]
			
			except:
				print("GPT FAIL")
				return random.choice(
					(
						"I'm sorry, I don't understand your question.",
						"Could you repharse your question?",
						"What you're trying to say is beyond my knowledge, sorry."
					)
				)

		return random.choice(data["intents"][self.classify[tag_result]]["responses"])
	

	def train_model(self) -> None:
		"""
		To train the model
		"""

		words  = []
		labels = []
		docs_x = []
		docs_y = []

		# Parsing the dataset-
		try:
			with open(self.dataset, "r") as intents:
				data = json.load(intents)

		except FileNotFoundError:
			return print("The intents file doesn't exist for training model")

		for intent in data["intents"]:
			for pattern in intent["patterns"]:
				tokenized_word = nltk.word_tokenize(pattern)	# Getting the root word
				words.extend(tokenized_word)
				docs_x.append(tokenized_word )
				docs_y.append(intent["tag"])
			
			if intent["tag"] not in labels:
				labels.append(intent["tag"])
			
		words = [self.stemmer.stem(w.lower()) for w in words if w not in self.ignore_chars] 	# The AI's vocabulary
		words = sorted(list(set(words)))	# Formatting; removing duplicates & rearranging words
		labels = sorted(labels)

		# Using bag-of-words method to convert it's vocabulary to a vector word count.
		training = []
		output   = []

		out_empty = [0 for _ in range(len(labels))]

		for x, doc in enumerate(docs_x):
			bag = []

			stemmed_words = [self.stemmer.stem(w.lower()) for w in doc]

			for w in words:
				if w in stemmed_words:
					bag.append(1)
					continue

				bag.append(0)
		
			output_row = out_empty.copy()
			output_row[labels.index(docs_y[x])] = 1

			training.append(bag)
			output.append(output_row)

		training = numpy.array(training)
		output   = numpy.array(output)

		with open(rf"model\model_versions\MV{self.MODEL_NO}\train_data\training_data_{self.MODEL_NO}.bin", "wb") as training_data_file:
			pickle.dump((words, labels, training, output), training_data_file)
		
		with open(rf"model\model_versions\MV{self.MODEL_NO}\train_data\intents_classify_{self.MODEL_NO}.bin", "wb") as intents_classify_file:

			classify = {}

			for index, content in enumerate(data["intents"]):
				classify[content["tag"]] = index

			pickle.dump(classify, intents_classify_file)

		self.connect_model(training, output, "train")