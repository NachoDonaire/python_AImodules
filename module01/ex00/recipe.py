import datetime

class   Recipe:
    def __init__(self, name, cl, ct, i, d, rt):
        if (type(name) != str):
            print("type error");
            exit()
        if type(cl) != int:
            print("type error")
            exit()
        if (int(cl) > 5 or int(cl) < 1):
            cl = "cooking level goes from 1 to 5"
        if type(ct) != datetime.datetime:
            print("type error")
        if (type(i) != list):
            print("type error")
        if d and type(d) != str:
            print("typer error")
        elif not d:
            d = "No description for this recipe"
        if type(rt) != str:
            print("type error")
        self.name = name
        if int(cl) <= 0 or int(cl) > 5:
            print("cooking level out of range")
            exit()
        self.cooking_level = cl
        self.cooking_time = ct
        self.ingredients = i
        self.description = d
        self.recipe_type = rt
    def __str__(self):
        txt = "The recipe is {}, with a cooking level of {} and a time to cook of {}. Ingredients: {}. {}. this recipe is a {}".format(self.name, self.cooking_level, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt
