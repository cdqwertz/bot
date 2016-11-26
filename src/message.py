import datetime

class message:
	def __init__(self, text, user="", time = datetime.datetime.now):
		self.text_raw = text
		self.text = text
		self.user = user
		self.time = time
