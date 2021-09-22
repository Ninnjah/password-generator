def get_number():
    while True:
        try:
            return int(input("Enter password length: "))
        except ValueError:
            print("You should enter a number")


def yes_or_not(msg):
    print(msg)
    while True:
        answer = input("Enter y/n: ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("You should enter y/n")
