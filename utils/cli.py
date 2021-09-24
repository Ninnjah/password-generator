def get_number(msg: str) -> int:
    while True:
        try:
            number: int = int(input(msg))
            if number <= 0:
                raise ValueError

            return number

        except ValueError:
            print("You should enter a positive number")


def yes_or_not(msg: str) -> bool:
    print(msg)
    while True:
        answer: str = input("Enter y/n: ")
        if answer.lower() in "yn":
            return answer.lower() == "y"
        else:
            print("You should enter y/n")
