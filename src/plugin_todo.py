from message import *
import compare, random, datetime

class plugin_todo():
	def __init__(self):
		pass
		
	def load(self, bot):
		pass
		
	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""
		
		if compare.compare(text, ["i", ["still", ""], ["need", "have"], "to", "[...]"]):
			values = compare.compare(text, ["i", ["still", ""], ["need", "have"], "to", "[...]", "[...]", "[...]", "[...]", "[...]", "[...]", "[...]", "[...]", "[...]", "[...]"])
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []
				
			msg.user.data["todo:list"].append(values["[...]"].strip().replace("my ", "your "))
			out = "I added \"" + values["[...]"].strip() + "\" to your todo list!"
		elif compare.compare(text, ["what", "do", "i", ["still", ""], ["have", "need"], ["to", "todo"], ["do", ""], ["today", ""]]):
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []
				
				
			if len(msg.user.data["todo:list"]) == 0:
				out = "You do not have any items on your TODO list."
			else:
				out = "You still need to " + ", ".join(msg.user.data["todo:list"]) + "."
		else:
			return None
			
		return message(out, bot)
