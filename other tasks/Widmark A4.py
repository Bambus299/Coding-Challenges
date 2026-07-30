m = input("wie viel wiegst du?")
V = input("wie viel ml hast du getrunken?")
e =input("wie hoch ist der alk anteil?")

p = 0.8


A = int(V) * float(e) * p

gender = input("Bist du männlich oder weiblich oder ein Kind? (M/F/K) : ")

if gender == "M":
    c = A / (int(m) * 0.7)
elif gender == "F":
    c = A / (int(m) * 0.6)
else:
    c = A / (int(m) * 0.8)
print("Dein Blutalkoholgehalt beträgt: ", c)