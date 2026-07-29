letters = input("gib deinen Buchstaben salat ein: ")
searchphrase = "Code"

c = letters.count("c")
o = letters.count("o")
d = letters.count("d")
e = letters.count("e")

if c > o :
    while c > o :
        c = (c - 1)
        print(c)

if o > d :
    while o > d :
        d = (d - 1)
        print(d)

if d > e :
    while d > e :
        d = (d - 1)
        print(d)

if e > c :
    while e > c :
        e = (e - 1)
        print(e)

if c < o :
    while c < o :
        o = (o - 1)
        print(c)

if o < d :
    while o < d :
        d = (d - 1)
        print(d)

if d < e :
    while d < e :
        e = (e - 1)
        print(d)

if e < c :
    while e < c :
        c = (c - 1)
        print(e)

if e == c :
    print(c)
    print(o)
    print(d)
    print(e)
