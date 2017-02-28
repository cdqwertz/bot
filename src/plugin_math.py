from message import *
import compare, random, datetime

class plugin_math():
	def __init__(self):
		pass

	def is_number(self, string):
		if string.startswith("-") and string[1:].isdigit():
			return True
		elif string.isdigit():
			return True
		elif "." in string:
			a = string.split(".")
			if len(a) == 2:
				return self.is_number(a[0]) and self.is_number(a[1])
		return False

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		vars = {"<user_name>" : msg.user.name, "<bot_name>" : bot.name}

		if msg.intent == "math_multiply":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				vars["<a>"] = values["<a>"]
				vars["<b>"] = values["<b>"]
				vars["<c>"] = str(a*b)

				out = bot.language.get_answer("math_multiply", vars)

		elif msg.intent == "math_add":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				vars["<a>"] = values["<a>"]
				vars["<b>"] = values["<b>"]
				vars["<c>"] = str(a+b)

				out = bot.language.get_answer("math_add", vars)

		elif msg.intent == "math_subtract":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				vars["<a>"] = values["<a>"]
				vars["<b>"] = values["<b>"]
				vars["<c>"] = str(a-b)

				out = bot.language.get_answer("math_subtract", vars)

		elif msg.intent == "math_divide":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				vars["<a>"] = values["<a>"]
				vars["<b>"] = values["<b>"]
				vars["<c>"] = str(a/b)

				out = bot.language.get_answer("math_divide", vars)
		else:
			return None


		return message(out, bot)
