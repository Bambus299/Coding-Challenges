print("Das Tamagotchi Spiel")


Base_Stat_Change = 15 
High_Stat_Change = 20
Health_Stat_Change = 10

Stat_Full = 100
Stat_Empty = 0

hunger = Stat_Full
happiness = Stat_Full
health = Stat_Full
sleep = Stat_Full
Days = Stat_Empty


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

    if hunger > 100:
        hunger = Stat_Full

    if happiness > 100:
        happiness = Stat_Full

    if sleep > 100:
        sleep = Stat_Full

    if health > 100:
        health = Stat_Full

    if hunger <= 0 or happiness <= 0 or sleep <= 0:
        health -= Health_Stat_Change
        print("Dein Tamagotchi ist in einem schlechten Zustand. Gesundheit sinkt um 10.")

    if hunger <= 0:
        hunger = Stat_Empty

    if happiness <= 0:
        happiness = Stat_Empty

    if sleep <= 0:
        sleep = Stat_Empty

    if health <= 0:
        print("Dein Tamagotchi ist gestorben.")
        print("Dies sind deine finalen Werte:")
        status(hunger, happiness, health, sleep, Days)


    
    