import post
import json
import req

start_data = req.get_data("04")
print(start_data)
start_data.sort(key=lambda x: x["reindeer"])

all_solution = ""

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
    
    
    
    #all_solution = int(all_solution)
    print(name)
    print(maxMoves)

    all_solution += f"\{'name': '{name}','maxMoves': {int(maxMoves)}\}"


print(json.dumps("[" + all_solution + "]" ))


#solutionResult =  post.post_data("04", json.dumps(all_solution))
#print(solutionResult)