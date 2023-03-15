from Account import Account

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        if  type(new_account) == Account:
            if (self.iscorrupt(new_account)):
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
        print(new_account.__dict__)
        if (indicator >= 1):
            return False
        if  suma % 2 == 0:
            return False
        return True

if  __name__ == "__main__":
    banco = Bank()
    acc = Account("evaristo")
    print(str(banco.iscorrupt(acc)))

