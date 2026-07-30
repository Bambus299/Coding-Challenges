def Geschenksliste(liste) :
    korrigierte_Liste = []

    for char in liste :
        start = char.find("(")
        end = char.find(")")

        needed = char[:start]
        include = char[start + 1 : end]

        turn = ""
        for char in include :
            turn = char + turn 

        complete = (needed + turn).capitalize()
        korrigierte_Liste.append(complete)

    korrigierte_Liste.sort()
    return korrigierte_Liste
Wunschliste = ["Stoff(reit)","au(ot)"]
result = Geschenksliste(Wunschliste)

print(result)