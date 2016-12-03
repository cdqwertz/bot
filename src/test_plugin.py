from message import *
import compare, random, datetime

class plugin_default():
	def __init__(self):
		pass
		
	def on_msg(self, bot, msg):
		text = msg.text
		return message(text, bot)
