def roll_call_dwarves(dwarves):
    num = 1
    for i in dwarves:
        print(f"{num}. {i}")
        num += 1

def summon_captain_planet(dwarves):
    return [i.capitalize() + "!" for i in dwarves]

    

def long_planeteer_calls(calls):
    for i in calls:
        if len(i) > 4:
            return True
    
    return False


def find_the_cheese(cheese):
    for i in cheese:
        if i == "cheddar" or i == "gouda" or i == "camembert":
            return i
    
    return None

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients))
