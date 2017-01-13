from bot import *
from user import *

class chatroom:
	def __init__(self, bot, users = []):
		self.users = users
		self.bot = bot
		self.history = []
	
	def add_user(self, user):
		self.users.append(user)
		
	def get_user(self, name, create_new=False):
		for my_user in self.users:
			if my_user.name == name:
				return my_user
			
		if create_new == True:
			my_user = user(name)
			self.add_user(my_user)
			return my_user
		else:	
			return None
		
	def on_msg(self, msg):
		self.history.append(msg)
		out = self.bot.on_msg(msg)
		
		if out:
			self.history.append(out)
			
		return out
