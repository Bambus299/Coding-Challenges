import post
import req
import json

start_data = req.get_data("09")
print("Rohdaten vom Server:", start_data)


stores_raw = start_data["stores"]

all_items = [item for sublist in stores_raw for item in sublist]


low_inventory = []


for item in set(all_items):
    anzahl = all_items.count(item)
    
    if anzahl < 3:
        low_inventory.append(item)


low_inventory.sort()

solution_dict = {
    "missingItems": low_inventory
}
print("Sende diese Lösung:", solution_dict)



solutionResult = post.post_data("09",low_inventory)
print("Server-Antwort:", solutionResult)
