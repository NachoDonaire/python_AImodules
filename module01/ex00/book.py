import datetime

def error_msg:
    print("error")
    exit()


class   Book:
    def __init__(self, name, lu, cd, rl):
        if (type(name) != str):
            error_msg()
        if (type(lu) != datetime):
            error_msg()
        if (type(cd) != datetime):
            error_msg()
        if (type(rl) != dict):
            error_msg
        self.name = name
        self.last_update = lu
        self.creation_date = cd
        self.recipes_list = rl
    def get_recipe_by_name(self, name):
        print(self.recipes_list[name])
        return (self.recipes_list[name])
    def get_recipe_by_type(self, recipe_type):

