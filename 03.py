letters = input("gib deinen Buchstaben salat ein: ")

letters = letters.lower()

c = letters.count("c")
o = letters.count("o")
d = letters.count("d")
e = letters.count("e")

min(c,o,d,e)
print(min(c,o,d,e))
