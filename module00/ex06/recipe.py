import sys

def error_msg():
    print("error")
    exit()

def print_name(cookbook):
    for e in cookbook:
        print(e)
def print_details(cookbook):
    s = input("Which recipe would you like to see?:\n")
    for e in cookbook[s]:
        print(cookbook[s][e])
def del_recipe(cookbook):
    s = input("Which recipe would you like to remove?:\n")
    cookbook.pop(s)

def add_recipe(cookbook):
    name = input("Enter a name:\n")
    ingredients = []
    ingre = input("Enter ingredients:\n")
    ingredients.append(ingre)
    while (ingre):
        ingre = input()
        ingredients.append(ingre)

    meal = input("Enter a meal type:\n")
    time = input("Enter a preparation time:\n")
    if not (str(time).isdigit()):
        print("error")
        exit ()
    dictionary = {}
    dictionary["ingredients"] = ingredients
    dictionary["meal"] = meal
    dictionary["time"] = time
    cookbook[name] = dictionary
    


cookbook = {}

cookbook1 = {"ingredients" : ["jamon", "pan", "queso", "tomate"], "meal" : "almuerzo", "prep_time" : 10}
cookbook2 = {"ingredients" : ["harina", "azucar", "huevos"], "meal" : "postre", "prep_time" : 60}
cookbook3 = {"ingredients" : ["aguacate", "ruculas", "espinacas"], "meal" : "almuerzo", "prep_time" : 15}

cookbook = {"bocadillo" : cookbook1, "tarta" : cookbook2, "ensalada" : cookbook3}

if __name__ == "__main__":
    print("Welcome to ajete. Choose an option please:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the Cookbook")
    print("5: Quit")

    option = "hola"
    while (1):
        option = input("> ")
        if not (str(option).isdigit()):
            print("please, valid number")
        elif int(option) >= 6 or int(option) <= 0:
            print("please, valid number")
        elif int(option) == 1:
            add_recipe(cookbook)
        elif int(option) == 2:
            del_recipe(cookbook)
        elif int(option) == 3:
             print_details(cookbook)
        elif int(option) == 4:
              print_name(cookbook)
        elif int(option) == 5:
             exit()


