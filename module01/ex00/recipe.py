import datetime

class   recipe:
    def __init__(self, name, cl, ct, i, d, rt):
        if (type(name) != str):
            print("type error");
            exit()
        if type(cl) != int:
            print("type error")
            exit()
        if type(ct) != datetime.datetime:
            print("type error")
        if (type(i) != list):
            print("type error")
        if d and type(d) != str:
            print("typer error")
        if type(rt) != str:
            print("type error")
        self.name = name
        self.cooking_level = cl
        self.cooking_time = ct
        self.ingredients = i
        self.description = d
        self.recipe_type = rt
    def __str__(self):
        txt = "The recipe is {}, with a cooking level of {} and a time to cook of {}. Ingredients: {}. {}. this recipe is a {}".format(self.name, self.cooking_level, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt

if __name__ == "__main__":
    name = "josias"
    cl = 1
    ct = datetime.datetime.now()
    i = ["tomato", "onion"]
    d = "This meal is tomatonion"
    rt = "entrante"
    r = recipe(name, cl, ct,i, d, rt)
    print(str(r))
