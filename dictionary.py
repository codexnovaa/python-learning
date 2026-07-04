#Dictionary -- key value {key:value} pairs
#               ordered and changable. no duplicates

capitals = {"Switzerland": "Bern",
            "USA": "Washington D.C,",
            "Japan": "Tokyo",
            "South Korea": "Seoul",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals.get("Japan"))

#if capitals.get("Switzerland"):
    #print("This capital exist")
#else:
    #print("This capital in your list not included")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detriot"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#for key in keys:
    #print(key)
    
#values = capitals.values()
#for value in values:
    #print(value)
num = 0
    
items = capitals.items()
for item in items:
    for value in item[num]:
        print(value, end="")
    print()

#print(capitals)