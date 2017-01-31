from message import *
import compare, random, datetime

class plugin_math():
	def __init__(self):
		pass

	def load(self, bot):
		bot.language.register_pattern("math_multiply", compare.pattern_to_string(
						["<a>", ["times", "multiplied", "*"], ["by", ""], "<b>", ["equals", "=", ""]]
						))

		bot.language.register_pattern("math_add", compare.pattern_to_string(
						["<a>", ["plus", "added", "+"], ["to", ""], "<b>", ["equals", "=", ""]]
						))

		bot.language.register_pattern("math_subtract", compare.pattern_to_string(
						["<a>", ["minus", "-"], "<b>", ["equals", "=", ""]]
						))

		bot.language.register_pattern("math_divide", compare.pattern_to_string(
						["<a>", ["divided", "/"], ["by", ""], "<b>", ["equals", "=", ""]]
						))

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

		if msg.intent == "math_multiply":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				out = values["<a>"] + " times " + values["<b>"] + " equals " + str(a * b)

		elif msg.intent == "math_add":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				out = values["<a>"] + " plus " + values["<b>"] + " equals " + str(a + b)

		elif msg.intent == "math_subtract":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				out = values["<a>"] + " minus " + values["<b>"] + " equals " + str(a - b)

		elif msg.intent == "math_divide":
			values = msg.intent_data

			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])

				out = values["<a>"] + " divided by " + values["<b>"] + " equals " + str(a / b)
		else:
			return None


		return message(out, bot)
