from message import *
from bot import *
from user import *
from chatroom import *

import plugin_default

my_bot = bot("bot")
my_bot.add_plugin(plugin_default.plugin_default())

my_chatroom = chatroom(my_bot)

my_user = user("test")
my_chatroom.add_user(my_user)

run = True
while run:
	i = input("you: ")
	if not(i.lower().strip() == "quit" or i.lower().strip() == "exit"):
		msg = message(i, my_user)
		out = my_chatroom.on_msg(msg)
		if out:
			print(out.user.name + ": " + out.text)
	else:
		run = False
