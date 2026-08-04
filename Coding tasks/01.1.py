import req 
import json
import post

start_data = req.get_data("01")
print(start_data)

start = json.dumps(start_data)

erster_wert = start_data[0]["value"]
zweiterer_wert = start_data[1]["value"]
dritter_wert = start_data[2]["value"]
vierter_wert = start_data[3]["value"]

erster_Zustand = start_data[0]["currentFormat"]
zweiter_Zustand = start_data[1]["currentFormat"]
dritter_Zustand = start_data[2]["currentFormat"]
vierter_Zustand = start_data[3]["currentFormat"]

erste_methode = start_data[0]["targetFormat"]
zweite_methode = start_data[1]["targetFormat"]
dritte_methode = start_data[2]["targetFormat"]
vierte_methode = start_data[3]["targetFormat"]

print(erster_wert, zweiterer_wert, dritter_wert, vierter_wert)
print(erster_Zustand, zweiter_Zustand, dritter_Zustand, vierter_Zustand)
print(erste_methode, zweite_methode, dritte_methode, vierte_methode)

def convert(value, current_format, target_format):

    if current_format == "DAY" and target_format == "HOUR":
        return value * 24
    elif current_format == "DAY" and target_format == "MINUTE":
        return value * 1440
    elif current_format == "DAY" and target_format == "SECOND":
        return value * 86400
    elif current_format == "HOURS" and target_format == "DAY":
        return value / 24
    elif current_format == "HOUR" and target_format == "MINUTE":
        return value * 60
    elif current_format == "HOUR" and target_format == "SECOND":
        return value * 3600
    elif current_format == "MINUTE" and target_format == "DAY":
        return value / 1440
    elif current_format == "MINUTE" and target_format == "HOUR":
        return value / 60
    elif current_format == "MINUTE" and target_format == "SECOND":
        return value * 60
    elif current_format == "SECOND" and target_format == "DAY":
        return value / 86400
    elif current_format == "SECOND" and target_format == "HOUR":
        return value / 3600
    elif current_format == "SECOND" and target_format == "MINUTE":
        return value / 60
    else:
        raise ValueError("Invalid format conversion")

result1 = convert(erster_wert, erster_Zustand, erste_methode)
result2 = convert(zweiterer_wert, zweiter_Zustand, zweite_methode)
result3 = convert(dritter_wert, dritter_Zustand, dritte_methode)
result4 = convert(vierter_wert, vierter_Zustand, vierte_methode)



solution1 = int(result1)
solution2 = int(result2)
solution3 = int(result3)
solution4 = int(result4)

solution = [solution1, solution2, solution3, solution4]
#json_result = json.dumps(solution)
#print(json_result)

solutionResult =  post.post_data("01", solution)
print(solutionResult)
