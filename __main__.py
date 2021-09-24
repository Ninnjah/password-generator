import os
import string
import secrets
from typing import List

from utils import cli


def generate_password(length: int, alphabet: tuple, separator: str = "") -> str:
    return separator.join(secrets.choice(alphabet) for _ in range(length))


def config_words_pass() -> None:
    file_path: str = "./dictionaries"
    file_list: List[str] = [x for x in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, x))]

    file_name = os.path.join(file_path, cli.choose("Choose dict file: ", file_list))
    with open(file_name, "r", encoding="utf-8") as f:
        word_list: tuple = tuple(_.strip() for _ in f.readlines())

    pass_length = cli.get_number("Enter words count in password: ")
    print(generate_password(pass_length, word_list, separator="-"))


def config_pass() -> None:
    raw_alphabet: str = string.ascii_lowercase

    pass_length = cli.get_number("Enter password length: ")

    if cli.yes_or_not("Will the password contain capital letters?"):
        raw_alphabet += string.ascii_uppercase

    if cli.yes_or_not("Will the password contain digits?"):
        raw_alphabet += string.digits

    if cli.yes_or_not("Will the password contain special symbols?"):
        symbols = input("Enter special symbols: ")
        raw_alphabet += symbols

    alphabet: tuple = tuple(set(raw_alphabet))

    print(generate_password(pass_length, alphabet))


if __name__ == "__main__":
    input()
