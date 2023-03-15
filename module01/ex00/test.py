from book import Book
from recipe import Recipe
import datetime

if __name__ == "__main__":
    name = "josias"
    cl = 1
    ct = datetime.datetime.now()
    i = ["tomato", "onion"]
    d = ""
    rt = "entrante"
    r = Recipe(name, cl, ct,i, d, rt)
    rl = {"starter" : "pato", "launch" : "cumita", "dessert" : "fishy"}
    book = Book("Libro de cocina",ct, ct, rl)
    book.add_recipe(r)
    book.get_recipe_by_name("josias")
    book.get_recipe_by_type("entrante")
