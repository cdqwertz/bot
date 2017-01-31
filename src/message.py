import datetime

class message:
	def __init__(self, text, user="", time = datetime.datetime.now):
		self.text_raw = text
		self.text = text
		self.user = user
		self.time = time
		self.intent = ""
		self.intent_data = {}

	def get_intent(self, language):
		name, data = language.get_intent(self.text)
		self.intent = name
		self.intent_data = data
