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
	
	def on_msg(self, bot, msg):
		text = msg.text
		out = ""
		
		if compare.compare(text, ["<a>", ["times", "multiplied", "*"], ["by", ""], "<b>", ["equals", "=", ""]]):
			values = compare.compare(text, ["<a>", ["times", "multiplied", "*"], ["by", ""], "<b>", ["equals", "=", ""]])
			
			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])
				
				out = values["<a>"] + " times " + values["<b>"] + " equals " + str(a * b)
				
		elif compare.compare(text, ["<a>", ["plus", "added", "+"], ["to", ""], "<b>", ["equals", "=", ""]]):
			values = compare.compare(text, ["<a>", ["plus", "added", "+"], ["to", ""], "<b>", ["equals", "=", ""]])
			
			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])
				
				out = values["<a>"] + " plus " + values["<b>"] + " equals " + str(a + b)
				
		elif compare.compare(text, ["<a>", ["minus", "-"], "<b>", ["equals", "=", ""]]):
			values = compare.compare(text, ["<a>", ["minus", "-"], "<b>", ["equals", "=", ""]])
			
			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])
				
				out = values["<a>"] + " minus " + values["<b>"] + " equals " + str(a - b)
				
		elif compare.compare(text, ["<a>", ["divided", "/"], ["by", ""], "<b>", ["equals", "=", ""]]):
			values = compare.compare(text, ["<a>", ["divided", "/"], ["by", ""], "<b>", ["equals", "=", ""]])
			
			if self.is_number(values["<a>"]) and self.is_number(values["<b>"]):
				a = float(values["<a>"])
				b = float(values["<b>"])
				
				out = values["<a>"] + " divided by " + values["<b>"] + " equals " + str(a / b)
		else:
			return None
			
			
		return message(out, bot)
