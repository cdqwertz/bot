from message import *
import compare, random, datetime

class plugin_default():
	def __init__(self):
		pass
		
	def on_msg(self, bot, msg):
		text = msg.text
		out = ""
		
		if compare.compare(text, [["hi", "hello", "hey"], [bot.name, ""]]):
			out = random.choice(["hello", "hi", "hey"]) + " " + msg.user.name + random.choice(["!", ".", ""])
		elif compare.compare(text, [["bye"], [bot.name, ""]]) or compare.compare(text, [["see"], ["you"], ["soon", ""]]):
			out = random.choice(["bye", "see you soon"]) + random.choice(["!", ""])
		elif compare.compare(text, [["what", "whats", "what's"], ["is", ""], "the", "time"]):
			hour = str(datetime.datetime.now().hour) 
			hour = (2-len(hour)) * "0" + hour
			minute = str(datetime.datetime.now().minute)
			minute = (2-len(minute)) * "0" + minute
			out = "It is " + hour + ":" + minute + random.choice(["!", "."])
		elif compare.compare(text, [["what", "whats", "what's"], ["is", ""], ["the", "today's", "todays"], "date", ["today", ""]]):
			year = str(datetime.datetime.now().year) 
			month = str(datetime.datetime.now().month)
			day = str(datetime.datetime.now().day)
			out = "It is the " + day + " " + month + " " + year + random.choice(["!", "."])
		else:
			return None
			
		return message(out, bot)
