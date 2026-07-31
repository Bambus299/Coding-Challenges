print("Das Tamagotchi Spiel")

hunger = 100
happiness = 100
health = 100
sleep = 100
Days = 0

Base_Stat_Change = 5 
High_Stat_Change = 10


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
        hunger += High_Stat_Change
        health += Base_Stat_Change
        happiness += Base_Stat_Change   
        sleep -= Base_Stat_Change
    elif action == "spielen":
        happiness += 10
        health -= Base_Stat_Change
        hunger -= Base_Stat_Change
        sleep -= Base_Stat_Change
    elif action == "schlafen":
        sleep += High_Stat_Change
        health += Base_Stat_Change
        hunger -= Base_Stat_Change
        happiness -= Base_Stat_Change
    elif action == "nichts":
        hunger -= Base_Stat_Change
        happiness -= Base_Stat_Change
        health -= Base_Stat_Change
        sleep -= Base_Stat_Change
    elif action == "beenden":
        print("Du hast das Spiel beendet.")
        health -= 100
        print("Dies sind deine finalen Werte:")
        status(hunger, happiness, health, sleep, Days)  
    
        break
    elif health <= 0:
        print("Dein Tamagotchi ist gestorben.")
        break
    if health > 0 and action != "status" and action != "beenden" and action != "":
        Days = Days + 1
        print("Tag: ", Days)

    if hunger < 20:
        print("Dein Tamagotchi ist hungrig.")

    if happiness < 20:
        print("Dein Tamagotchi ist unglücklich.")

    if sleep < 20:
        print("Dein Tamagotchi ist müde.")

    if health < 20:
        print("Dein Tamagotchi ist krank.")
        


    
    