from message import *
from bot import *
from user import *
from chatroom import *

#my_bot = bot("bot", language = compare.language("patterns/patterns_de.txt", "entities/entities_de.txt", "answers/answers_de.txt"))
my_bot = bot("bot")
my_bot.load_plugins()
my_bot.event("loaded")

my_chatroom = chatroom(my_bot)

my_user = user("test")
my_chatroom.add_user(my_user)

run = True
while run:
	i = input("you: ")
	if not(i.lower().strip() == "q" or i.lower().strip() == "quit" or i.lower().strip() == "exit"):
		msg = message(i.lower(), my_user)
		out = my_chatroom.on_msg(msg)
		if out:
			print(out.user.name + ": " + out.text)
	else:
		my_bot.event("quit")
		run = False
