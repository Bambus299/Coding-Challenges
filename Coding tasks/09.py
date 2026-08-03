stores = [
    ["Puppe", "Fahrrad", "Spiel", "Puppe"],
    ["Auto", "Auto", "Puppe", "Fahrrad"],
    ["Ball", "Fahrrad", "Auto", "Puppe"]
]

stores = [item for sublist in stores for item in sublist]


def InventoryCheck(item_count):
    if item_count < 3:
        return True
    else:
        return False



if InventoryCheck(stores.count("Auto")):
    print("Du hast zu wenig Autos.")

if InventoryCheck(stores.count("Ball")):
    print("Du hast zu wenig Bälle.")

if InventoryCheck(stores.count("Fahrrad")):
    print("Du hast zu wenig Fahrräder.")

if InventoryCheck(stores.count("Puppe")):
    print("Du hast zu wenig Puppen.")

if InventoryCheck(stores.count("Spiel")):
    print("Du hast zu wenig Spiele.")


