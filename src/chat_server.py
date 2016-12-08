#TODO : support multiple user

from message import *
from bot import *
from user import *
from chatroom import *

import plugin_default
import plugin_math
import plugin_todo

import http.server, urllib
from urllib.parse import urlparse

my_bot = bot("bot")
my_bot.add_plugin(plugin_default.plugin_default())
my_bot.add_plugin(plugin_math.plugin_math())
my_bot.add_plugin(plugin_todo.plugin_todo())

my_chatroom = chatroom(my_bot)

my_user = user("test")
my_chatroom.add_user(my_user)

f = open("html/chat.html", "r")
html_blueprint = f.read()
f.close()

class requestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		global my_chatroom, my_user, my_bot, html_blueprint
		
		msg = urlparse(self.path).query
		if msg.startswith("message="):
			msg = msg[8:]
		
		msg = urllib.parse.unquote(msg.replace("+", " "))
		
		if msg == ":clear":
			my_chatroom.history = []
		else:
			out = my_chatroom.on_msg(message(msg.lower(), my_user))
		
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		
		m = ""
		for i in my_chatroom.history:
			if i.user.name == my_bot.name:
				m += "<div class=\"bot\">" + i.text + "</div>\n"
			else:
				m += "<div class=\"user\">" + i.text + "</div>\n"
		
		self.wfile.write(html_blueprint.replace("<!-- messages -->", m).encode("utf-8"))
		return

try:
	server = http.server.HTTPServer(('', 8080), requestHandler)
	server.serve_forever()
except KeyboardInterrupt:
	server.socket.close()
