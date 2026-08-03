def pruefe_flughoehen(sequenzen_liste):
    ergebnisse = []
    
    for seq in sequenzen_liste:
        if len(seq) % 2 == 0:
            ergebnisse.append(False)
            continue

        a = seq[0]
        x_max = (len(seq) + 1) // 2

        x_werte = list(range(1, x_max + 1)) + list(range(x_max - 1, 0, -1))

        ist_korrekt = all(abs(a * (x**2) - ist_wert) < 0.0001 for x, ist_wert in zip(x_werte, seq))
        ergebnisse.append(ist_korrekt)
        
    return ergebnisse


calculations = [
    (1, 4, 1),
    (0.5, 2, 4.5, 2, 0.5),
    (2, 3, 4, 4, 3, 2),
    (1, 4, 9, 16, 25, 16, 9, 4, 1)
]

print( pruefe_flughoehen(calculations))

