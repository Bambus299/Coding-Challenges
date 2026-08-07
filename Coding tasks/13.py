Divider = "#"
line = "|"
import req
import post
import json

def zeichne_geschenke_tabelle(geschenke_liste):
    geschenke_sortiert = sorted(geschenke_liste, key=lambda x: x['qty'], reverse=True)
    
    
    header_geschenk = "Geschenk"
    header_anzahl = "Anzahl"
    
    max_gift_len = max(len(item['gift']) for item in geschenke_sortiert)
    max_gift_len = max(max_gift_len, len(header_geschenk))
     
    max_qty_len = max(len(str(item['qty'])) for item in geschenke_sortiert)
    max_qty_len = max(max_qty_len, len(header_anzahl))
    
    col1_width = max_gift_len  
    col2_width = max_qty_len + 1
    l1 = "-" * (col1_width)
    l2 = "-" * (col2_width-1)   
    horizontale_linie1 = "#" * (col1_width + col2_width)
    horizontale_linie = "-" * (col1_width + col2_width) 
    
    tabelle = []
      
    tabelle.append(Divider + horizontale_linie1 + Divider)
      
    header_zeile = f"{Divider}{header_geschenk:<{max_gift_len}}|{header_anzahl:<{max_qty_len}}{Divider}"
    tabelle.append(header_zeile)
      
    tabelle.append(Divider + l1 + line + l2 + Divider)
      
    for item in geschenke_sortiert:
        geschenk_name = item['gift']
        anzahl_wert = item['qty']
        zeile = f"{Divider}{geschenk_name:<{max_gift_len}}|{anzahl_wert:<{max_qty_len}}{Divider}"
        tabelle.append(zeile)
       
    tabelle.append(Divider + horizontale_linie1 + Divider)
       
    return tabelle
start_data = req.get_data("13")
riddle_data = start_data
print(start_data)

tabellen_ansicht = zeichne_geschenke_tabelle(riddle_data)
print(json.dumps(tabellen_ansicht))

answer = post.post_data("13", json.dumps(tabellen_ansicht))
print(answer)

