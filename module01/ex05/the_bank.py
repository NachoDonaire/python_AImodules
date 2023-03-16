from Account import Account

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        if  type(new_account) == Account:
            self.error = -2
            for name in self.accounts:
                if name.name == new_account.name:
                    print("corrupta")
                    self.accounts.append(new_account)
                    return False
            self.accounts.append(new_account)
            return True
        else:
            print("error: new account must be Account object")
            return False

    def iscorrupt(self, new_account):
        suma = 0
        indicator = 0
        sub_i = 0;
        for element in new_account.__dict__:
            if str(element)[0] == 'b':
                indicator +=1
            elif str(element).startswith("zip"[:3]) or str(element).startswith("addr"[:4]):
                sub_i +=1
            suma += 1
        suma += 1
        if (indicator >= 1 or sub_i < 1):
            if indicator >= 1:
                self_error = -1
            if sub_i < 1:
                self.error = 0
            return False
        if  suma % 2 == 0:
            self.error = 1
            return False
        if new_account.id == None or new_account.name == None or new_account.value == None:
            if new_account.id == None:
                self.error = "id"
            elif new_account.name == None:
                self.error = "name"
            elif new_account.value == None:
                self.error = "value"
            return False
        if not type(new_account.name) == str:
            self.error = 3
            return False
        if not type(new_account.id) == int or type(new_account.id) == float:
            self.error = 5
            return False
        return True

    def transfer(self, origin, dest, amount):
        orig_index = -1
        dest_index = -1
        for acc,i in zip(self.accounts, range(len(self.accounts))):
            print(acc.name)
 #           print(origin)
  #          print(dest)
            if (acc.name == origin):
                orig_index = i
            elif (acc.name == dest):
                dest_index = i
        if orig_index == -1 or dest_index == -1:
            return False
        if self.iscorrupt(self.accounts[orig_index]) == False or self.iscorrupt(self.accounts[dest_index]) == False:
            print("invalid account")
            return False
        if not type(origin) == str or not type(dest) == str:
            print("origin and dest must be Account objects")
            return False
        if not type(amount) == float:
            print("no float as amount to transfer")
            return False
        if amount < 0:
            print("invalid amount")
            return False

        
        if self.accounts[orig_index].value < amount:
            print("not enough money")
            return False

        self.accounts[orig_index].value -= amount
        self.accounts[dest_index].value += amount
        return True

    def fix_account(self, name):
        index = -1
        for names, e in zip(self.accounts, range(len(self.accounts))):
            if (names.name == name):
                index = e
        if index == -1:
            return False
        if (self.iscorrupt(self.accounts[index]) == True):
            return False
        listy = self.accounts[index].__dict__
        if self.error > -2:
            if self.error == -1:
                listy = self.accounts[index].__dict__
                for e in listy:
                    if e.startswith("b"[:1]):
                        del self.accounts[index].e
            elif self.error == 0:
                 self.accounts[index].zip = "0005-777"
            elif self.error == 1:
                self.accounts[index].tucker = 23
            elif self.error == "id" or self.error == 5:
                self.accounts[index].id = len(self.accounts) + 1
            elif self.error == "name" or self.error == 3:
                self.accounts[index].name = "Wallace"
            elif self.error == "value":
                self.accounts[index].value = 0
        return True
