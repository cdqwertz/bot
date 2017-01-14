from message import *
import compare

class bot:
	def __init__(self, name = "", language = compare.language("patterns/patterns_en.txt", "entities/entities_en.txt")):
		self.name = name
		self.plugins = []
		self.users = []
		self.history = []
		self.language = language
		
	def add_plugin(self, plugin):
		self.plugins.append(plugin)
		plugin.load(self)
		
	def on_msg(self, msg):
		self.history.append(msg)
	
		output = ""
		
		if msg.user.wait_for_answer == -1:
			for i, plugin in enumerate(self.plugins):
				result = plugin.on_msg(self, msg, i)
				if result:
					output = result
					break
		else:
			output = self.plugins[self.wait_for_answer].answer(self, msg)
		
		self.history.append(output)
				
		return output
