from message import *
import compare, random, datetime

class plugin_fun():
	def __init__(self):
		pass

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		vars = {"<user_name>" : msg.user.name, "<bot_name>" : bot.name}

		if msg.intent == "fun_coin":
			if random.choice([0, 1]) == 0:
				out = bot.language.get_answer("fun_heads", vars)
			else:
				out = bot.language.get_answer("fun_tails", vars)

		elif msg.intent == "fun_dice":
			vars["<num>"] = random.choice("123456")
			out = bot.language.get_answer("fun_dice", vars)

		else:
			return None

		return message(out, bot)
