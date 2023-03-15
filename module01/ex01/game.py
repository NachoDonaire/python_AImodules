class   GotCharacter:
    def __init__(self, is_alive, first_name):
        self.is_alive = True
        self.first_name = name

class Stark(GotCharacter):
    def __init__(self, is_alive = True, first_name=None):
        super().__init__(is_alive=is_alive, first_name=first_name)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
        print(self.family_name)
    def die(self):
        self.is_alive = False
