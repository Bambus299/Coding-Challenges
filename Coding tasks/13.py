Divider = "#"

def zeichne_geschenke_tabelle(geschenke_liste):
    geschenke_sortiert = sorted(geschenke_liste, key=lambda x: x['qty'], reverse=True)
    
    
    header_geschenk = "Geschenk"
    header_anzahl = "Anzahl"
    
    max_gift_len = max(len(item['gift']) for item in geschenke_sortiert)
    max_gift_len = max(max_gift_len, len(header_geschenk))
     
    max_qty_len = max(len(str(item['qty'])) for item in geschenke_sortiert)
    max_qty_len = max(max_qty_len, len(header_anzahl))
    
    col1_width = max_gift_len + 2
    col2_width = max_qty_len + 2
        
    horizontale_linie = "-" * (col1_width + 1 + col2_width) 
    
    tabelle = []
      
    tabelle.append(Divider + horizontale_linie + Divider)
      
    header_zeile = f"{Divider} {header_geschenk:<{max_gift_len}} | {header_anzahl:<{max_qty_len}} {Divider}"
    tabelle.append(header_zeile)
      
    tabelle.append(Divider + horizontale_linie + Divider)
      
    for item in geschenke_sortiert:
        geschenk_name = item['gift']
        anzahl_wert = item['qty']
        zeile = f"{Divider} {geschenk_name:<{max_gift_len}} | {anzahl_wert:<{max_qty_len}} {Divider}"
        tabelle.append(zeile)
       
    tabelle.append(Divider + horizontale_linie + Divider)
       
    return "\n".join(tabelle)

riddle_data = [
    {"gift": "Auto", "qty": 12},
    {"gift": "Puppe", "qty": 10},
    {"gift": "playstation", "qty": 3}
]

tabellen_ansicht = zeichne_geschenke_tabelle(riddle_data)
print(tabellen_ansicht)
