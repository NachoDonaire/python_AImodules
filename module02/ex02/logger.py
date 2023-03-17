import time
import functools
from random import randint
import os

fd = open("machile.log", mode='w')

def log(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        retorno = function(*args, **kwargs)
        end_time = time.time()
        if (function.__name__ == "start_machine"):
            action = "Starting machine"
        elif (function.__name__ == "boil_water"):
            action = "Boiling water"
        elif function.__name__ == "make_coffee":
            action = "Preparing coffee"
        elif function.__name__ == "add_water":
            action = "Adding water"
        else:
            action = "Not recognized action"
        tucker = " " + str(action)
        final_spaces = 20 - len(tucker)
        complement_s = str(tucker) + str(" " * final_spaces)
        times = end_time - start_time
        texetx = "[ exec-time = {:.3f} ms ]".format(times)
        s = "(" + str(os.getlogin()) + ")Running:" +  str(complement_s) + str(texetx)
        fd.write(str(s) + "\n")
        return retorno
    return wrapper

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
