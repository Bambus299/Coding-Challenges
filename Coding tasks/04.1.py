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

    maxMoves = abs(left - right) + rightorleft

    print(name)
    print(maxMoves)

    all_solution += f"name: {name}\nmaxMoves: {maxMoves}\n"

    

print(all_solution)


solutionResult =  post.post_data("04", all_solution)
print(solutionResult)