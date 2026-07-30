def cleaning(wish : str, steps : list) -> str:
    for step in steps:
        task = step.get("task")
        char = step.get("char")
        
        if char not in wish:
            continue
            
        if task == "REMOVE_ALL":
            wish = wish.replace(char, "")
            
        elif task == "REMOVE_FIRST":
            wish = wish.replace(char, "", 1)
            
        elif task == "REMOVE_LAST":
            last_index = wish.rfind(char)
            wish = wish[:last_index] + wish[last_index + 1:]
            
    return wish

wish = input("gib deinen Wunsch ein: ")
tasks = input("gib deine Aufgaben ein: ")
characters = input("gib deine Zeichen ein: ")
steps = [
    {"task": tasks, "char": characters},
]

print(cleaning(wish, steps))