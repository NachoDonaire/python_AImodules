import datetime
from recipe import Recipe

class   Book:
    def __init__(self, name, lu, cd, rl):
        if (type(name) != str):
            print("error")
            exit()
        if (type(cd) != datetime.datetime):
            print("error")
            exit()
        if (type(rl) != dict):
            print("error")
            exit()
        self.name = name
        self.last_update = lu
        self.creation_date = cd
        self.recipes_list = rl
    def add_recipe(self, r):
        if (type(r) != Recipe):
            print("error: no recipe class as argument")
            exit()
        self.recipe = []
        self.recipe.append(r)
    def get_recipe_by_name(self, name):
        if not self.recipe:
            print("no recipes added yet")
            return
        for recipe, i in zip(self.recipe, range(len(self.recipe))):
            if (recipe.name == name):
                print(str(recipe))
                return recipe.name
        print("no matches")
            
    def get_recipe_by_type(self, name):
        if not self.recipe:
            print("no recipes added yet")
            return 
        for recipe, i in zip(self.recipe, range(len(self.recipe))):
            if (recipe.recipe_type == name):
                print(str(recipe))
                return(recipe.recipe_type)
        print("no matches")
        
