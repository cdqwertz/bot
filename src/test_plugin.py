from message import *

class test_plugin():
	def __init__(self):
		pass
		
	def on_msg(self, bot, msg):
		return message(msg.text, bot)
