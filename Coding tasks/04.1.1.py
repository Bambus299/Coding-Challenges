import post
import req

start_data = req.get_data("04")

# 1. Alphabetisch nach Rentiername sortieren
start_data.sort(key=lambda x: x["reindeer"])

rentier_liste = []

for reindeer_data in start_data: 
    name = str(reindeer_data["reindeer"])
    moves = str(reindeer_data["moves"])

    left = moves.count("<")
    rightorleft = moves.count("*")
    right = moves.count(">")

    # Mathematisch korrekte Berechnung der maximalen Distanz vom Startpunkt:
    # Wir berechnen das Maximum aus beiden Richtungen unter Einbeziehung der Joker
    max_links = left + rightorleft - right
    max_rechts = right + rightorleft - left
    
    maxMoves = max(max_links, max_rechts)

    reindeer_object = {
        "name": name,
        "maxMoves": maxMoves  # Sollte das fehlschlagen, hier str(maxMoves) nutzen
    }   
    rentier_liste.append(reindeer_object)

# Exakt der Schlüssel, den der Server in deiner Konsolenausgabe verlangt hat: "solution"
final_dict = {
    "solution": rentier_liste
}

print("Sende an Server:", final_dict)

solutionResult = post.post_data("04", final_dict)
print("Server-Antwort:", solutionResult)
