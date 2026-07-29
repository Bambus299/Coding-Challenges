reindeer = "Rudolph"
moves = input("Wie bewegt sich das rentier : ")

left = moves.count("<")
rightorleft = moves.count("*")
right = moves.count(">")

if left < right :
    maxMoves = (right + rightorleft - left)

if left > right :
    maxMoves = (left + rightorleft - right)

else :
    maxMoves = (rightorleft + left - right)

print(reindeer)
print(maxMoves)