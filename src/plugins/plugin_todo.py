from message import *
import compare, random, datetime

class plugin_todo():
	def __init__(self):
		pass

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		vars = {"<user_name>" : msg.user.name, "<bot_name>" : bot.name}

		if msg.intent == "todo_new":
			values = msg.intent_data
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []

			msg.user.data["todo:list"].append(values["[...]"].strip().replace("my ", "your "))
			vars["<item>"] = values["[...]"].strip()
			out = bot.language.get_answer("todo_new", vars)
		elif msg.intent == "todo_show":
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []


			if len(msg.user.data["todo:list"]) == 0:
				out = bot.language.get_answer("todo_empty", vars)
			else:
				vars["<items>"] = ", ".join(msg.user.data["todo:list"])
				out = bot.language.get_answer("todo_show", vars)

		elif msg.intent == "todo_done":
			if not("todo:list" in msg.user.data):
				msg.user.data["todo:list"] = []
			else:
				if len(msg.user.data["todo:list"]) == 0:
					out = bot.language.get_answer("todo_empty", vars)
				else:
					vars["<items>"] = ", ".join(msg.user.data["todo:list"])
					out = bot.language.get_answer("todo_show", vars)

		else:
			return None

		return message(out, bot)

def setup_plugin():
	return plugin_todo()
