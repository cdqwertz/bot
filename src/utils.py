def read_file(path):
	f = open(path, "r")
	s = f.read()
	f.close()
	return s
	
def save_file(path, string):
	f = open(path, "w")
	s = f.write(string)
	f.close()
