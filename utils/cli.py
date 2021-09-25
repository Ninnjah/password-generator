import sys
from typing import Any, List


def get_number(msg: str, min_: int = 0, max_: int = sys.maxsize) -> int:
    """Get number from user input

    :param msg: str - message for user
    :param min_: int = 0 - minimum value
    :param max_: int = sys.maxsize - maximum value

    :return int:
    """
    while True:
        try:
            number: int = int(input(msg))
            if min_ <= number <= max_:
                return number
            raise ValueError

        except ValueError:
            print(f"You should enter a number greater than {min_} and less than {max_}")


def choose(msg: str, list_: List[Any]) -> Any:
    """Get users select from the list

    :param msg: str - message for user
    :param list_: List[Any] - list for select

    :return Any:
    """
    for index, item in enumerate(list_, 1):
        print(f" [{index}] {item}")

    while True:
        index: int = get_number(msg, min_=1, max_=len(list_))
        if index <= len(list_):
            return list_[index - 1]
        else:
            print("The item with this number doesn't exist")


def yes_or_not(msg: str) -> bool:
    """Get yes or not answer from user

    :param msg: str - message for user

    :return bool:
    """
    print(msg)
    while True:
        answer: str = input("Enter y/n: ")
        if answer.lower() in "yn":
            return answer.lower() == "y"
        else:
            print("You should enter y/n")
