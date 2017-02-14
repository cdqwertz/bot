from compare import *

my_language = language("patterns/patterns_en.txt", "entities/entities_en.txt")
print(compare(input("> "), [["Hello", "Hi", "Hey"], "bot"], entities = my_language.entities))
