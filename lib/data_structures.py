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
    total_arr = []
    for each in spicy_foods:
        total_arr.append(each["name"])
    return total_arr
def get_spiciest_foods(spicy_foods):
    list_dict = []
    for each in spicy_foods:
        if each["heat_level"] > 5:
            list_dict.append(each)
    return list_dict


def print_spicy_foods(spicy_foods):
    for each in spicy_foods:
        print(each["name"] + " (" + each["cuisine"] + ") | Heat Level: " + "🌶" * each["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for each in spicy_foods:
        if each["cuisine"] == cuisine:
            return each

def print_spiciest_foods(spicy_foods):
    temp = get_spiciest_foods(spicy_foods)
    print_spicy_foods(temp)

def get_average_heat_level(spicy_foods):
    avg_int = 0
    avg_total = 0
    for each in spicy_foods:
        avg_int += 1
        avg_total += each["heat_level"]
    return avg_total/avg_int

def create_spicy_food(spicy_foods, spicy_food):
    temp = spicy_foods
    temp.append(spicy_food)
    return temp
