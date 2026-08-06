import post
import req
import json
def cleaning(wish : str, steps : list) -> str:
    for step in steps:
        task = step.get("task")
        char = step.get("char")
        
        if char not in wish:
            continue
            
        if task == "REMOVE_ALL":
            wish = wish.replace(char, "")
            
        elif task == "REMOVE_FIRST":
            wish = wish.replace(char, "", 1)
            
        elif task == "REMOVE_LAST":
            last_index = wish.rfind(char)
            wish = wish[:last_index] + wish[last_index + 1:]
            
    return wish

start_data = req.get_data("06")
print("Rohdaten vom Server:", start_data)

wishes_field = start_data["wishes"]
steps = start_data["reductionSteps"]

if isinstance(wishes_field, list):
    solution = [cleaning(single_wish, steps) for single_wish in wishes_field]
else:

    words = wishes_field.split()
    cleaned_words = [cleaning(w, steps) for w in words]
    solution = " ".join(cleaned_words) if len(cleaned_words) > 1 else cleaned_words[0]

print("Deine bereinigte Lösung:", solution)


solutionResult = post.post_data("06", solution)
print("Server-Antwort:", solutionResult)
