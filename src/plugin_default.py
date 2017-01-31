from message import *
import compare, random, datetime

class plugin_default():
	def __init__(self):
		pass

	def load(self, bot):
		bot.language.register_pattern("default_hello", compare.pattern_to_string(
						[["hi", "hello", "hey"], ["bot", ""]]
						))

		bot.language.register_pattern("default_bye", compare.pattern_to_string(
						[["bye", "bbl"]]
						))

		bot.language.register_pattern("default_see_you_soon", compare.pattern_to_string(
						["see", "you", ["soon", ""]]
						))

		bot.language.register_pattern("default_how_are_you", compare.pattern_to_string(
						["how", "are", "you", ["today", ""]]
						))

		bot.language.register_pattern("default_name", compare.pattern_to_string(
						["what", "is", "your", "name"]
						))

		bot.language.register_pattern("default_time", compare.pattern_to_string(
						[["what", "whats", "what's"], ["is", ""], "the", "time"]
						))

		bot.language.register_pattern("default_date", compare.pattern_to_string(
						[["what", "whats", "what's"], ["is", ""], ["the", "today's", "todays"], "date", ["today", ""]]
						))

		bot.language.register_pattern("default_location", "\"where\", (\"do\", \"are\"), \"you\", (\"live\", \"located\")")

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		if msg.intent == "default_hello":
			out = random.choice(["Hello", "Hi", "Hey"]) + " " + msg.user.name + random.choice(["!", ".", ""])

		elif msg.intent == "default_bye" or msg.intent == "default_see_you_soon":
			out = random.choice(["Bye", "See you soon"]) + random.choice(["!", ""])

		elif msg.intent == "default_how_are_you":
			out = random.choice(["I am fine!", "I am fine and you?"])

		elif msg.intent == "default_name":
			out = "My name is " + bot.name + "."

		elif msg.intent == "default_time":
			hour = str(datetime.datetime.now().hour)
			hour = (2-len(hour)) * "0" + hour
			minute = str(datetime.datetime.now().minute)
			minute = (2-len(minute)) * "0" + minute
			out = "It is " + hour + ":" + minute + random.choice(["!", "."])

		elif msg.intent == "default_date":
			year = str(datetime.datetime.now().year)
			month = str(datetime.datetime.now().month)
			day = str(datetime.datetime.now().day)
			out = "It is the " + day + " " + month + " " + year + random.choice(["!", "."])

		elif msg.intent == "default_location":
			out = "I live inside a computer."

		else:
			return None

		return message(out, bot)
