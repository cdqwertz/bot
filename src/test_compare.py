from compare import *
load_patterns("patterns/patterns_en.txt")

print(get_pattern("default_hello"))
print(compare(input("> "), get_pattern("default_hello")))
