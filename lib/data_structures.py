spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list = []
    pass
    for obj in spicy_foods:
        list.append(obj['name'])
    return list

def get_spiciest_foods(spicy_foods):
    list = []
    pass
    for obj in spicy_foods:
        if obj['heat_level'] > 5:
            list.append(obj)
    return list

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for obj in spicy_foods:
        if obj['cuisine'] == cuisine:
            return obj

def print_spiciest_foods(spicy_foods):
    pass
    list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(list)

def get_average_heat_level(spicy_foods):
    pass
    total = 0
    for obj in spicy_foods:
        total += obj['heat_level']
    total /= len(spicy_foods)
    return total

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
