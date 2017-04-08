from message import *
import compare

class bot:
	def __init__(self, name = "", language = compare.language("patterns/patterns_en.txt", "entities/entities_en.txt")):
		self.name = name
		self.plugins = []
		self.users = []
		self.history = []
		self.language = language
		self.events = {}

	def add_plugin(self, plugin):
		self.plugins.append(plugin)

		try:
			plugin.load(self)
			print("[info][" + plugin.__class__.__name__ + "] loaded")
		except AttributeError:
			print("[warning][" + plugin.__class__.__name__ + "] load() not found")

	def on(self, event, func):
		if event in self.events.keys():
			self.events[event].append(func)
		else:
			self.events[event] = [func]

	def event(self, event):
		if not(event in self.events.keys()):
			return
			
		for func in self.events[event]:
			func()

	def on_msg(self, msg):
		msg.get_intent(self.language)
		print(msg.intent, " ", msg.intent_data["score"])
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

		while len(self.history) > 20:
			self.history.pop(0)

		return output
