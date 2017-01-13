import socket, time
from message import *
from bot import *
from user import *
from chatroom import *

import plugin_default
import plugin_math
import plugin_todo

#setup irc
def send(text):
	global s
	print("[send] " + text, end = "")
	s.send(text.encode("utf-8"))

server = input("server: ")
port = 6667

nick = input("nick: ")
owner = input("owner: ")

print("\nHello " + owner + ".")
print("I will try to connect to the irc server \"" + server + "\" on port " + str(port) + " now.")
input("[Press Enter]")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
send(("USER " + nick + " " + nick + " " + nick + " :" + nick + "\r\n"))
send("NICK " + nick + "\r\n")

#setup bot
my_bot = bot(nick)
my_bot.add_plugin(plugin_default.plugin_default())
my_bot.add_plugin(plugin_math.plugin_math())
my_bot.add_plugin(plugin_todo.plugin_todo())

my_chatroom = chatroom(my_bot)
my_chatroom.add_user(user(owner))

run = True

while run:
	try:
		data = str(s.recv(1024 * 2).decode("utf-8"))
		print("[data] " + data)
		
		lines = data.split("\n")
		
		for line in lines:
			params = line.strip("\n\r ").split(" ")
	
			if data.find("PING") != -1:
				send("PONG " + params[1] + "\r\n")
					
			else:
				if line.startswith(":") and params[1].lower() == "privmsg":
					msg_user = line[1:line.find("!~")].strip(" ")
					msg_channel = params[2].strip(" ")
					msg_text = line[line.find(":", 1) + 1:].strip(" ")
					
					print("[msg] From:", msg_user, "Channel:", msg_channel, "Text:", msg_text)
					
					if msg_user == owner and msg_text.startswith("!"):
						parts = msg_text.split(" ")
						
						for i, part in enumerate(parts):
							parts[i] = part.strip("\r\n ").lower()
			
						print("[command]", parts[0])
						
						if parts[0] == "!join":
							send("JOIN " + parts[1] + "\r\n")
							
						if parts[0] == "!quit":
							run = False
					elif msg_channel == nick:
						my_user = my_chatroom.get_user(msg_user, True)
						out = my_chatroom.on_msg(message(msg_text, my_user))
						if out:
							send("PRIVMSG " + msg_user + " :" + out.text + "\r\n")
							
	
	except KeyboardInterrupt:
		run = False
		continue
		
	except Exception as e:
		print("[error]" + str(e))
		continue

time.sleep(0.1)	
send("QUIT :quit\r\n")
time.sleep(0.3)
s.close()
