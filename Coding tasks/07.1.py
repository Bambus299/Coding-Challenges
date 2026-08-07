import post
import req
import json

def calculate_max_parcels(parcels, maxpayload):
    sort = sorted(parcels, key=lambda x: x["weight"])
    count = 0
    total_weight = 0
    
    for parcel in sort:  
        weight = parcel["weight"]
        if total_weight + weight <= maxpayload:
            total_weight += weight
            count += 1
        else:
            break

    return count, total_weight


start_data = req.get_data("07")
print("Rohdaten vom Server:", start_data)

parcels = start_data["parcels"]
maxpayload = start_data["maxPayload"]

parcel_count, payload = calculate_max_parcels(parcels, maxpayload)

solution_dict = {
    "parcelCount": parcel_count,
    "payload": payload
}
print("Sende diese Lösung:", solution_dict)

solutionResult = post.post_data("07", solution_dict)
print("Server-Antwort:", solutionResult)