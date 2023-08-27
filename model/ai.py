import nltk
import numpy
import tensorflow
import random
import json

from nltk.stem.lancaster import LancasterStemmer
from typing import Literal

class Ai:
	def __init__(self) -> None:
		pass

	def train_ai(self, dataset:str = "intents.json") -> None:
		"""
		@dataset: The fiel location of the dataset over which the AI is going to train over
		"""
		stemmer = LancasterStemmer()

		words  = []
		labels = []
		docs_x = []
		docs_y = []

		try:
			with open(dataset, "r") as file:
				data = json.load(file)

		except FileNotFoundError:
			return print("The file doesn't exist")

		for intent in data["intents"]:
			for pattern in intent["patterns"]:

				try:
					tokenized_word = nltk.word_tokenize(pattern)
				except LookupError:
					nltk.download("punkt")
					tokenized_word = nltk.word_tokenize(pattern)
					
				words.extend(tokenized_word)
				docs_x.append(pattern)
				docs_y.append(intent["tag"])
			
			if intent["tag"] not in labels:
				labels.append(intent["tag"])
			
		words = [stemmer.stem(w.lower()) for w in words] 	# The AI's vocabulary
		words = sorted(list(set(words)))	# Formatting; removing duplicates & rearranging words
		labels = sorted(labels)

		print(words)

Ai().train_ai()