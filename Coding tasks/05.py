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
Wunschliste = ["S((ffti)ot)er', '(tuA)o', '((upp)P)e', 'Dr(ie)rad', 'Bau(ts)eine', 'B(la)l', '((tift)S)e', 'Bil(red)buch', 'Eis((nba)e)hn', 'Fa(rh)rad', 'Stap(tsle)eine', 'K(le(ch)su)tier', 'Bret(pst)iel', 'Kaufm(snna)laden', '(i(örsp)H)el', 'Baste((sch)l)ere"]
result = Geschenksliste(Wunschliste)

print(result)