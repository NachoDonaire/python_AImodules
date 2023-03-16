from Account import Account

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        if  type(new_account) == Account:
            if (self.iscorrupt(new_account) == False):
                return False
            for name in self.accounts:
                if name.name == new_account.name:
                    return False
            self.accounts.append(new_account)
            return True
        else:
            print("error: new account must be Account object")
            return False

    def iscorrupt(self, new_account):
        suma = 0
        indicator = 0
        for element in new_account.__dict__:
            if str(element)[0] == 'b':
                indicator +=1
            elif str(element).startswith("zip"[:3]) or str(element).startswith("addr"[:4]):
                indicator +=1
            suma += 1
        if (indicator >= 1):
            return False
        if  suma % 2 == 0:
            return False
        if new_account.id == None or new_account.name == None or new_account.value == None:
            return False
        if not type(new_account.name) == str:
            return False
        if not type(new_account.id) == int:
            return False
        if not type(new_account.id) == int or type(new_account.id) == float:
            return False
        return True

    def transfer(self, origin, dest, amount):
        if not type(origin) == Account or not type(dest) == Account:
            print("origin and dest must be Account objects")
            return False
        if not type(amount) == float:
            print("no float as amount to transfer")
            return False
        if amount < 0:
            print("invalid amount")
            return False
        if iscorrupt(origin) == False or iscorrupt(dest) == False:
            print("invalid account")
            return False
        if (origin.name == dest.name):
            return True
        if origin.value < amount:
            print("not enough money")
            return False
        origin.value -= amount
        dest.value += amount
        return True


if  __name__ == "__main__":
    banco = Bank()
    acc = Account("evaristo", "250")
    acc1 = Account("Tobias", "300")
    acc2 = Account("Jones", "400")
    banco.transfer
    print(banco.add(acc))
    print(banco.add(acc2))
    """
    print(str(banco.iscorrupt(acc)))
    print(str(banco.iscorrupt(acc1)))
    print(str(banco.iscorrupt(acc2)))
    """

