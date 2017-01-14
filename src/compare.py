import utils, random

class language:
	def __init__(self, path_patterns, path_entities):
		self.patterns = {}
		self.entities = {}
		
		self.path = path_patterns
		self.path_entities = path_entities
		
		self.load_patterns()
		self.load_entities()

	def load_patterns(self):
		string = utils.read_file(self.path)
		lines = string.split("\n")
		for line in lines:
			if line != "":
				parts = line.split("=", 1)
				if len(parts) == 2:
					self.patterns[parts[0].strip()] = parts[1].strip()
		
	def save_patterns(self):
		string = ""
		keys = list(self.patterns.keys())
		keys.sort()
		for k in keys:
			string += k + " = " + self.patterns[k] + "\n"
		
		utils.save_file(self.path, string)
	

	def get_pattern(self, name):
		if name in self.patterns:
			return parse_pattern(self.patterns[name])
		
	def register_pattern(self, name, pattern):
		self.patterns[name] = pattern
		self.save_patterns()
		
	def train(self, name, s):
		pattern = parse_pattern(self.patterns[name])
		string = parse_string(s)
		i = 0
		j = 0
		while j < len(string):
			word = string[j]
		
			if i < len(pattern):
				if type(pattern[i]) == type([]):
					if not(word in pattern[i]) and not("" in pattern[i]) and not("?" in pattern[i]):
						pattern[i].append(word)
						
				else:
					if not(pattern[i].startswith("<")) and not(pattern[i].startswith("[")) and not(pattern[i] == "?"):
						if pattern[i] != word:
							if j+1 < len(string) and get_pattern_len(pattern) < len(string):
								found = False
								w = string[j+1]
								k = i
								while k < len(pattern) and not(found):
									if type(pattern[k]) == type([]):
										print(word, " type(pattern[k]) == type([])")
										if w in pattern[k]:
											pattern.insert(i, [word, ""])
											found = True
									else:
										if w == pattern[k]:
											pattern.insert(i, [word, ""])
											found = True
									k += 1
								
								if not(found):
									a = pattern[i]
									pattern[i] = [a, word]
								
							else:
								a = pattern[i]
								pattern[i] = [a, word]
					
			else:
				pattern.append(word)
				
			i += 1
			j += 1
		
		self.patterns[name] = pattern_to_string(pattern)
		self.save_patterns()
		
	def load_entities(self):
		string = utils.read_file(self.path_entities)
		lines = string.split("\n")
		name = ""
		for line in lines:
			if line != "":
				if line.startswith("\t"):
					s = line.strip("\t ")
					if s != "":
						if s.startswith("(") and s.endswith(")"):
							pass
						else:
							parts = s.split(" ")
							word_name = parts[0]
							word_value = parts[1]
							self.entities[name][word_name] = word_value
				else:
					name = line
					self.entities[name] = {}

def get_pattern_len(pattern):
	length = 0
	for i in pattern:
		if type(i) == type([]):
			if not("" in i):
				length += 1
		else:
			length += 1
			
	return length
	
def pattern_to_string(pattern):
	string = []
	for i in pattern:
		if type(i) == type([]):
			string.append("(" + pattern_to_string(i) + ")")
		else:
			string.append("\"" + i + "\"")
			
	return ", ".join(string)
	
def parse_pattern(p):
	pattern = []
	
	is_str = False
	my_str = ""
	x = 0
	y = 0
	for token in p:
		if y == 0:
			if not(is_str):
				if token == "(" or token == "{":
					y += 1
					my_str = ""
				elif token == "\"":
					is_str = True
					my_str = ""
			else:
				if token == "\"":
					is_str = False
					pattern.append(my_str)
					my_str = ""
				else:
					my_str += token
		else:
			if token == "(" or token == "{":
				if y == 0:
					my_str = ""
				else:
					my_str += token
					
				y += 1
			elif token == ")":
				y -= 1
				
				if y == 0:
					pattern.append(parse_pattern(my_str))
					my_str = ""
				else:
					my_str += token
			elif token == "}":
				y -= 1
				
				if y == 0:
					a = parse_pattern(my_str)
					a.append("")
					pattern.append(a)
					my_str = ""
				else:
					my_str += token
			else:
				my_str += token
		x += 1
	
	return pattern

def parse_string(string_raw):
	string = string_raw.split()
	
	x = 0
	for w in string:
		string[x] = w.strip(".,!? ")
		x += 1
	
	return string
	
def compare_words(word, pattern):
	score = 0.0
	i = 0
	for letter in word:
		if len(pattern) > i and letter == pattern[i]:
			score += 1.0
		elif len(pattern) > i and i > 0 and letter == pattern[i-1]:
			i -= 1
			score += 0.5
		
		i += 1
	
	try:
		return (score/float(len(word)))
	except ZeroDivisionError:
		print("Zero division!")
		return 0.0

def compare(string_raw = "",  pattern = None, pattern_raw = None, entities = None):
	if not(pattern):
		pattern = parse_pattern(pattern_raw)
		
	string = parse_string(string_raw)
	
	i = 0
	j = 0
	result = True
	output = {}
	while i < len(string) and j < len(pattern):
		if type(pattern[j]) == type([]):
			m = False
			for w in pattern[j]:
				if compare_words(w, string[i]) > 0.6:
					m = True
					break
				elif w == "?":
					m = True
					break
				elif w == "":
					m = True
					i -= 1
					break
				elif w.startswith("<") and w.endswith(">"):
					output[pattern[j]] = string[i]
					m = True
					break
					
			result = result and m
			if result == False:
				return False
		else:
			m = False
			if compare_words(pattern[j], string[i]) > 0.6:
				m = True
			elif pattern[j] == "?":
				m = True
			elif pattern[j] == "":
				m = True
				i -= 1
			elif pattern[j].startswith("<") and pattern[j].endswith(">"):
				output[pattern[j]] = string[i]
				m = True
			elif pattern[j].startswith("[") and pattern[j].endswith("]"):
				if not(pattern[j] in output):
					output[pattern[j]] = ""
				output[pattern[j]] += string[i] + " "
				m = True
			
			result = result and m
			#print(" -> ", result)
			if result == False:
				return False
		
		i += 1
		j += 1
		
	if entities:
		for word in string:
			for k in entities.keys():
				for w in entities[k].keys():
					if compare_words(word, w) > 0.6:
						output[k] = entities[k][w]
		
	output["result"] = result
	return output

def generate_text(pattern):
	string = []
	for i in pattern:
		if type(i) == type([]):
			string.append(random.choice(i))
		else:
			string.append(i)
			
	return " ".join(string)

