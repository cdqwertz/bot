from message import *
import compare, random, datetime

class plugin_todo():
	def __init__(self):
		pass

	def load(self, bot):
		bot.language.register_pattern("todo_new", compare.pattern_to_string(
						["i", ["still", ""], ["need", "have"], "to", "[...]"]
						))

		bot.language.register_pattern("todo_show", compare.pattern_to_string(
						["what", "do", "i", ["still", ""], ["have", "need"], ["to", "todo"], ["do", ""], ["today", ""]]
						))

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		if msg.intent == "todo_new":
			values = msg.intent_data
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []

			msg.user.data["todo:list"].append(values["[...]"].strip().replace("my ", "your "))
			out = "I added \"" + values["[...]"].strip() + "\" to your todo list!"
		elif msg.intent == "todo_show":
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []


			if len(msg.user.data["todo:list"]) == 0:
				out = "You do not have any items on your todo list."
			else:
				out = "You still need to " + ", ".join(msg.user.data["todo:list"]) + "."
		else:
			return None

		return message(out, bot)
