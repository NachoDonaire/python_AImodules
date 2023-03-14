import  random
def initial_msg():
    print("Hello and welcome to interactive guessing game!!")
    print("You have to type a number between 1 and 99 to find out the secret number")
    print("Type 'exit' to quit")
    print("Good luck!")

def douglas_reference():
    print("Douglas douglas douglas!! congrats!! everything senses 42!")
if __name__ == "__main__":
    initial_msg()

    secret = random.randint(1, 99)
    number = secret + 1;
    while (int(number) != secret):
        number = input("What is your guessed number?:\n")
        if (number == "exit"):
            print("exit")
            exit()
        if not (str(number).isdigit()):
            print("This is not a number")
            number = secret + 1
        elif (int(number) < secret):
            print("Too low!")
        elif (int(number) > secret):
            print("Too high!")
        elif(int(number) == secret and secret == 42):
            douglas_reference()
        else:
            print("You won!!")


