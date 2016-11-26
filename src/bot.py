from message import *

class bot:
	def __init__(self, name = ""):
		self.name = name
		self.plugins = []
		self.users = []
		self.history = []
		
	def add_plugin(self, plugin):
		self.plugins.append(plugin)
		
	def on_msg(self, msg):
		self.history.append(msg)
	
		output = ""
		for plugin in self.plugins:
			result = plugin.on_msg(self, msg)
			if result:
				output = result
				break
				
		return output
