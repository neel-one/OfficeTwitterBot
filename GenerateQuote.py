import random
import json


quotes = []
with open("quote_list.json", "r") as quotefile:
	quotes = json.load(quotefile)


class Quote:

	def __init__(self):
		self.index = random.randint(0,len(quotes))
		self.quote = quotes[self.index]


	def DeleteQuote(self):
		quotes.pop(self.index)
		with open("quote_list.json", "w") as quotefile:
			json.dump(quotes, quotefile)