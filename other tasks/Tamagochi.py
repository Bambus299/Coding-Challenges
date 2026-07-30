print("Das Tamagotchi Spiel")

hunger = 100
happiness = 100
health = 100
sleep = 100
Days = 0


def status(hunger, happiness, health, sleep, Days):
    print("Hunger: ", hunger)
    print("Happiness: ", happiness)
    print("Health: ", health)
    print("Sleep: ", sleep)
    print("Days: ", Days)



while health > 0 :
    print("Dies sind deine möglichkeiten:")
    print(">Essen")
    print(">Spielen")
    print(">Schlafen")
    print(">Status")
    print(">Nichts")
    print(">Beenden")
    action = input("Was möchtest du tun? : ")

    if action == "status":
        status(hunger, happiness, health, sleep, Days)
    elif action == "essen":
        hunger += 10
        health += 5
        happiness += 5
        sleep -= 5
    elif action == "spielen":
        happiness += 10
        health -= 5
        hunger -= 5
        sleep -= 5
    elif action == "schlafen":
        sleep += 10
        health += 5
        hunger -= 5
        happiness -= 5
    elif action == "nichts":
        hunger -= 5
        happiness -= 5
        health -= 5
        sleep -= 5
    elif action == "beenden":
        print("Du hast das Spiel beendet.")
        health -= 100
        break
    elif health <= 0:
        print("Dein Tamagotchi ist gestorben.")
        break
    elif health > 0 and action != "status":
        Days = Days + 1
        print("Tag: ", Days)

        


    
    