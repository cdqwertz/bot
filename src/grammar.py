class sentence:
	def __init__(self, string = "", parts = [], is_question = False):
		self.string = string
		self.parts = parts
		self.is_question = is_question
		
	def get_verb(self):
		for w in self.parts:
			if w.part_type == "verb":
				return w
		return None
		
	def get_subject(self):
		for w in self.parts:
			if w.part_type == "subject":
				return w
		return None
	
	def build(self):
		blueprint = ["subject", "auxiliary_verb", "verb", "object", "location", "time"]
		if self.is_question:
			blueprint = ["auxiliary_verb", "subject",  "verb", "object"]
		
		output = []
		for i in blueprint:
			for p in self.parts:
				if p.part_type == i:
					output.append(str(p))
					break
			
		string = " ".join(output)
		self.string = string
		return string
		

class part:
	def __init__(self, words = [], part_type = "subject"):
		self.words = words
		self.part_type = part_type
		
	def __str__(self):
		return " ".join(map(str, self.words))

class word:
	def __init__(self, name = "", word_type = "noun"):
		self.name = name
		self.word_type = word_type
		
	def __str__(self):
		return self.name
