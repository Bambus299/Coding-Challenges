from collections import deque

def finde_weihnachtsmann_weg(karte):
    reihen = len(karte)
    spalten = len(karte[0]) if reihen > 0 else 0
    
    start, ziel = None, None
    
    # Positionen bestimmen und Zeichen bereinigen
    for r in range(reihen):
        for s in range(spalten):
            wert = karte[r][s].strip()
            if wert == "+":
                start = (r, s)
            elif wert == "!":
                ziel = (r, s)
                
    if not start or not ziel:
        return "Start (+) oder Ziel (!) nicht gefunden."
        
    # Erlaubte Symbole für den Weg
    begehbar = {"°", "•", "!"}
    
    # Richtungen: (Reihe_Änderung, Spalte_Änderung, Richtung)
    richtungen = [
        (-1, 0, 'U'),  # Oben
        (1, 0, 'D'),   # Unten
        (0, -1, 'L'),  # Links
        (0, 1, 'R')    # Rechts
    ]
    
    queue = deque([(start[0], start[1], "")])
    besucht = {start}
    
    while queue:
        r, s, pfad = queue.popleft()
        
        if (r, s) == ziel:
            return pfad
            
        for dr, dc, richtung in richtungen:
            nr, nc = r + dr, s + dc
            
            if 0 <= nr < reihen and 0 <= nc < spalten:
                nachbar_wert = karte[nr][nc].strip()
                
                if nachbar_wert in begehbar and (nr, nc) not in besucht:
                    besucht.add((nr, nc))
                    queue.append((nr, nc, pfad + richtung))
                    
    return "Kein gültiger Pfad zum Schlitten gefunden."

# Deine Karte als spielbares zweidimensionales Array
deine_karte = [
    ["#", "+", "#"],
    ["#", "°", "#"],
    ["#", "°", "!"],
    ["#", "#", "#"]
]

# Ausgabe des Ergebnisses
ergebnis = finde_weihnachtsmann_weg(deine_karte)
print(f"Der richtige Pfad ist: {ergebnis}")
