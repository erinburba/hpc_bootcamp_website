import os
import pickle
from paperqa import Docs

class Chatbot:

	def __init__(self, pickle_filename) -> None:
		self.api_key = os.environ.get("OPENAI_API_KEY")
		if not self.api_key:
			print("no api key!!!")
		with open(pickle_filename, "rb") as f:
			self.docs = pickle.load(f)
		# self.docs = Docs(llm='gpt-3.5-turbo')
		# self.docs.add_url('https://www.whitehouse.gov/environmentaljustice/justice40/')
		# self.docs.add("energyjustice.pdf")
    

	def query(self, query):
		return self.docs.query(query)



if __name__ == "__main__":
	bot = Chatbot("test_docs.pkl")
	print(bot.query("What is the Justice40 initiative?"))