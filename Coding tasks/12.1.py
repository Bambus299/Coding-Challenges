def evaluiere_links_nach_rechts(ausdruck):
    rechnung, erwartetes_ergebnis_str = ausdruck.split('=')
    erwartetes_ergebnis = int(erwartetes_ergebnis_str.strip())
    
    rechnung = rechnung.replace(" ", "")
    
    zahlen = []
    operatoren = []
    
    temporaere_zahl = ""
    for zeichen in rechnung:
        if zeichen in "+-*/":
            operatoren.append(zeichen)
            zahlen.append(int(temporaere_zahl))
            temporaere_zahl = ""
        else:
            temporaere_zahl += zeichen

    if temporaere_zahl:
        zahlen.append(int(temporaere_zahl))
        
    ergebnis = zahlen[0]
    
    for i in range(len(operatoren)):
        op = operatoren[i]
        naechste_zahl = zahlen[i + 1]
        
        if op == '+':
            ergebnis += naechste_zahl
        elif op == '-':
            ergebnis -= naechste_zahl
        elif op == '*':
            ergebnis *= naechste_zahl
        elif op == '/':
            ergebnis //= naechste_zahl 
            
    return ergebnis == erwartetes_ergebnis

def pruefe_rechnungen(liste_von_rechnungen):
    return [evaluiere_links_nach_rechts(r) for r in liste_von_rechnungen]

calculations = [
    "1+1=2",   
    "5+8=10",  
    "9-3*3=18"  
]

print(pruefe_rechnungen(calculations))
