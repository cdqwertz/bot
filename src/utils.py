def read_file(path):
	f = open(path, "r")
	s = f.read()
	f.close()
	return s
