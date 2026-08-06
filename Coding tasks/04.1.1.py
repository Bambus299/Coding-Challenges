import post
import json
import req

start_data = req.get_data("04")
print(start_data)
start_data.sort(key=lambda x: x["reindeer"])

json_solution = []

for reindeer_data in start_data : 
    name = str(reindeer_data["reindeer"])
    moves = str(reindeer_data["moves"])

    left = moves.count("<")
    rightorleft = moves.count("*")
    right = moves.count(">")

    additionalMovesWithWildCard =  (rightorleft - abs(left - right)) / 2
    maxMoves = additionalMovesWithWildCard
    if(left > right) :
        maxMoves  += left
    
    else :
        maxMoves  += right

    reindeer_object = {
        "maxMoves": int(maxMoves),
        "name": name
        
    }   
    json_solution.append(reindeer_object)



print(json_solution)


solutionResult =  post.post_data("04", json_solution)
print(solutionResult)