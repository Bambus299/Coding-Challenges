def equation(parcels, maxpayload) :
    sort = sorted(parcels)
    weight = 0
    count = 0
    total_weight = 0
    print(sort)

    for weight in sort:  
        if total_weight < (maxpayload - weight):
           total_weight = (total_weight + weight)
           print(total_weight)
           count += 1
        else:
            break

    return count, total_weight

parcels = [5, 4, 7, 5]

maxpayload = 22
count_total, weight_total = equation(parcels, maxpayload)
print(f"Anzahl Pakete: {count_total}")
print(f"Gesamtgewicht: {weight_total}")
print(maxpayload)
