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

def compare(string_raw = "",  pattern = None, pattern_raw = None):
	if not(pattern):
		pattern = parse_pattern(pattern_raw)
		
	string = parse_string(string_raw)
	
	i = 0
	j = 0
	result = True
	while i < len(string) and j < len(pattern):
		print("I: ", i, " J: ", j)
		if type(pattern[j]) == type([]):
			m = False
			for w in pattern[j]:
				if w == string[i]:
					m = True
					break
				elif w == "?":
					m = True
					break
				elif w == "":
					m = True
					i -= 1
					break
					
			result = result and m
			if result == False:
				return False
		else:
			m = False
			if pattern[j] == string[i]:
				m = True
			elif pattern[j] == "?":
				m = True
			elif pattern[j] == "":
				m = True
				i -= 1
			
			result = result and m
			print(" -> ", result)
			if result == False:
				return False
		
		i += 1
		j += 1
	return result
	
	
	
