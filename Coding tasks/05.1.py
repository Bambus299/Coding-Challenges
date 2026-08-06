import post
import req
import json


def Auflösen(word : str) :
    Character =list(word)
    stack =[]
    for i, char in enumerate(Character):
        if char == "(":
            stack.append(i)
        elif char == ")" :
            start = stack.pop()
            Character[start + 1 : i] = reversed(Character[start + 1 : i ])

    sol_word = "".join([c for c in Character if c not in ("(", ")")])
    return sol_word.capitalize()
    
start_data = req.get_data("05")
print(start_data)

presents = start_data if isinstance(start_data, list) else start_data.get("gifts", start_data)

solution = [Auflösen(article)for article in presents]
solution.sort()
print(solution)


    
solutionResult =  post.post_data("05", solution)
print(solutionResult)