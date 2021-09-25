import sys
from typing import Any, List


def get_number(msg: str, min_: int = 0, max_: int = sys.maxsize) -> int:
    while True:
        try:
            number: int = int(input(msg))
            if min_ <= number <= max_:
                raise ValueError

            return number

        except ValueError:
            print(f"You should enter a number greater than {min_} and less than {max_}")


def choose(msg: str, list_: List[Any]) -> Any:
    for index, item in enumerate(list_, 1):
        print(f" [{index}] {item}")

    while True:
        index: int = get_number(msg)
        if index <= len(list_):
            return list_[index - 1]
        else:
            print("The item with this number doesn't exist")


def yes_or_not(msg: str) -> bool:
    print(msg)
    while True:
        answer: str = input("Enter y/n: ")
        if answer.lower() in "yn":
            return answer.lower() == "y"
        else:
            print("You should enter y/n")
