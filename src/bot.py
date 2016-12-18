from message import *
import compare

class bot:
	def __init__(self, name = "", language = compare.language("patterns/patterns_en.txt")):
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
		for plugin in self.plugins:
			result = plugin.on_msg(self, msg)
			if result:
				output = result
				break
		
		self.history.append(output)
				
		return output
