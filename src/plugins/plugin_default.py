from message import *
import compare, random, datetime

class plugin_default():
	def __init__(self):
		pass

	def on_msg(self, bot, msg, i):
		text = msg.text
		out = ""

		vars = {"<user_name>" : msg.user.name, "<bot_name>" : bot.name}

		if msg.intent == "default_hello":
			out = bot.language.get_answer("default_hello", vars)

		elif msg.intent == "default_bye" or msg.intent == "default_see_you_soon":
			out = bot.language.get_answer("default_bye", vars)

		elif msg.intent == "default_how_are_you":
			out = bot.language.get_answer("default_how_are_you", vars)

		elif msg.intent == "default_name":
			out = bot.language.get_answer("default_name", vars)

		elif msg.intent == "default_time":
			hour = str(datetime.datetime.now().hour)
			hour = (2-len(hour)) * "0" + hour
			minute = str(datetime.datetime.now().minute)
			minute = (2-len(minute)) * "0" + minute
			vars["<hour>"] = hour
			vars["<minute>"] = minute
			out = bot.language.get_answer("default_time", vars)

		elif msg.intent == "default_date":
			year = str(datetime.datetime.now().year)
			month = str(datetime.datetime.now().month)
			day = str(datetime.datetime.now().day)
			vars["<day>"] = day
			vars["<month>"] = month
			vars["<year>"] = year
			out = bot.language.get_answer("default_date", vars)

		elif msg.intent == "default_location":
			out = bot.language.get_answer("default_location", vars)

		else:
			return None

		return message(out, bot)

def setup_plugin():
	return plugin_default()
