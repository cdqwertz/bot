import compare

class plugin_test():
	def __init__(self):
		pass

	def on_msg(self, bot, msg, i):
		return None

def setup_plugin():
	print("SETUP!")
	return plugin_test()
