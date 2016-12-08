from bot import *
from user import *

class chatroom:
	def __init__(self, bot, users = []):
		self.users = users
		self.bot = bot
		self.history = []
	
	def add_user(self, user):
		self.users.append(user)
		
	def on_msg(self, msg):
		self.history.append(msg)
		out = self.bot.on_msg(msg)
		
		if out:
			self.history.append(out)
			
		return out
