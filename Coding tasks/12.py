erste = int(input("Gib eine Zahl ein: "))
zweite = int(input("Gib eine weitere Zahl ein: "))

Rechenaufgabe = input("Welche Rechenoperation möchtest du durchführen? (+, -, *, /): ")

def berechne(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Fehler: Division durch Null"
    else:
        return "Ungültige Rechenoperation"
    

berechne(erste, zweite, Rechenaufgabe)
print(berechne(erste, zweite, Rechenaufgabe))