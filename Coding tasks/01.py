def conversion(days: int, rate: int):
    days * rate
    

days = input("How many days : ")
mode = input("In Hours,Minutes or Seconds : ")
conversion_hours= 24
conversion_minutes= 24 * 60
conversion_seconds= 24 * 60 * 60

if mode == "Hours":
    solution = conversion(int(days), conversion_hours)
    #solution = (int(days) * conversion_hours)
elif mode == "Minutes":
    solution = conversion(int(days), conversion_minutes)
else :
    solution = conversion(int(days), conversion_seconds)


print(solution)

