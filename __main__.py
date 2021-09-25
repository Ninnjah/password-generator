import os
import string
import secrets
from typing import Generator, List, Union

from utils import cli
from utils import ascii_text


def generate_password(length: int, alphabet: tuple, separator: str = "") -> str:
    return separator.join(secrets.choice(alphabet) for _ in range(length))


def save_to_file(filename: str, data: Union[List[str], Generator]) -> None:
    with open(filename, "a+", encoding="utf-8") as f:
        f.writelines([x+"\n" for x in data])


def config_words_pass() -> None:
    file_path: str = "./dictionaries"
    file_list: List[str] = [x for x in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, x))]

    file_name: str = os.path.join(file_path, cli.choose("Choose dict file: ", file_list))
    with open(file_name, "r", encoding="utf-8") as f:
        word_list: tuple = tuple(_.strip() for _ in f.readlines())

    separation_symbol: str = input("Enter separation symbol: ")
    pass_length: int = cli.get_number("Enter words count in password: ")
    passwords_count: int = cli.get_number("Enter count of passwords: ")

    passwords: List[str] = [
        generate_password(pass_length, word_list, separator=separation_symbol) for _ in range(passwords_count)
    ]
    print("Your password is")
    for password in passwords:
        print(password)

    if cli.yes_or_not("Do you want to save passwords in file?"):
        file: str = input("Enter file name (default-\"passwords\"): ") or "password"
        save_to_file(file+".txt", passwords)


def config_pass() -> None:
    raw_alphabet: str = string.ascii_lowercase

    pass_length: int = cli.get_number("Enter password length: ")

    if cli.yes_or_not("Will the password contain capital letters?"):
        raw_alphabet += string.ascii_uppercase

    if cli.yes_or_not("Will the password contain digits?"):
        raw_alphabet += string.digits

    if cli.yes_or_not("Will the password contain special symbols?"):
        symbols: str = input("Enter special symbols: ")
        raw_alphabet += symbols

    alphabet: tuple = tuple(set(raw_alphabet))
    passwords_count: int = cli.get_number("Enter count of passwords: ")

    passwords: List[str] = [generate_password(pass_length, alphabet, separator="") for _ in range(passwords_count)]
    print("Your password is")
    for password in passwords:
        print(password)

    if cli.yes_or_not("Do you want to save passwords in file?"):
        file: str = input("Enter file name (default-\"passwords\"): ") or "password"
        save_to_file(file+".txt", passwords)


if __name__ == "__main__":
    print(ascii_text.greet)
    if cli.choose("Choose password type: ",
                  ["Default password", "Password from words"]) == "Default password":
        config_pass()
    else:
        config_words_pass()
