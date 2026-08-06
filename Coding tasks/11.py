import req
import post 

start_value = 0
aenderung_value = 1

def lichter_check(lichterketten):
    ergebnis = []
    
    for kette in lichterketten:
        aenderungen_start_rot = start_value
        aenderungen_start_gruen = start_value
        
        for index, farbe in enumerate(kette):
            erwartet_rot = "RED" if index % 2 == 0 else "GREEN"
            if farbe != erwartet_rot:
                aenderungen_start_rot += aenderung_value
                
            erwartet_gruen = "GREEN" if index % 2 == 0 else "RED"
            if farbe != erwartet_gruen:
                aenderungen_start_gruen += aenderung_value
        
        ergebnis.append(min(aenderungen_start_rot, aenderungen_start_gruen))

    print(ergebnis) 
    solution = post.post_data("11" ,ergebnis)
    print(solution)
    
    
   
start_data = req.get_data("11")
print(start_data)
fairylights = start_data
lichter_check(fairylights)






