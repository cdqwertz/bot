import compare

def train():
	path_patterns = input("patterns: ")
	path_entities = input("entities: ")
	
	if path_patterns == "":
		path_patterns = "patterns/patterns_en.txt"

	if path_entities == "":
		path_entities = "entities/entities_en.txt"

	lang = compare.language(path_patterns, path_entities)

	pattern = ""
	while not(pattern in lang.patterns):
		pattern = input("pattern: ")
	
	run = True
	while run:
		string = input("> ").lower()
	
		if string == ":q" or string == "exit" or string == "quit":
			run = False
		elif string == ":n" or string == ":new":
			n = input("name: ")
			lang.register_pattern(n, "")
			pattern = n
		elif string == ":p" or string == ":pattern":
			while not(pattern in lang.patterns):
				pattern = input("pattern: ")
		elif string == ":c" or string == ":clear":
			lang.patterns[pattern] = ""
			lang.save_patterns()
		else:
			lang.train(pattern, string)
			print(lang.patterns[pattern])
		
train()
		
