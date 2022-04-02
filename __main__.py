import os
import re
import string
import secrets
from typing import Generator, List, Union

from utils import cli
from utils import ascii_text


def generate_password(length: int, alphabet: tuple, separator: str = "", mode: str = "standard") -> str:
    """Generates password

    :param length: int - length of password in symbols or words
    :param alphabet: tuple - tuple of symbols or words
    :param separator: str = "" - symbol between symbols or words
    :param mode: str = "standard":
        "standard" - standard generating password
        "nu_duplicate" - generating password without duplicate symbols or words

    :return str:
    """
    if mode == "standard":
        return separator.join(secrets.choice(alphabet) for _ in range(length))
    elif mode == "no_duplicate":
        alphabet: list = list(alphabet)
        return separator.join(alphabet.pop(secrets.randbelow(len(alphabet))) for _ in range(length))


def save_to_file(filename: str, data: Union[List[str], Generator]) -> None:
    """Saves data to file

    :param filename: str - absolute or relative path to file
    :param data: Union[List[str], Generator] - list or generator of data

    :return None:
    """
    # Delete forbidden symbols from filename
    find_str = re.escape("\"?*|\\/:><")
    filename = re.sub(f"[{find_str}]", "", filename)

    # Write data to filename
    with open(filename, "a+", encoding="utf-8") as f:
        f.writelines([x+"\n" for x in data])


def config_words_pass() -> None:
    """Configures setting to generate password from words"""
    # Path to dictionaries dir
    file_path: str = "./dictionaries"
    # Files from file_path
    file_list: List[str] = [x for x in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, x))]
    # Default mode
    mode: str = "standard"

    # Read words from dictionary
    file_name: str = os.path.join(file_path, cli.choose("Choose dict file: ", file_list))
    with open(file_name, "r", encoding="utf-8") as f:
        word_list: tuple = tuple(_.strip() for _ in f.readlines())

    # Config password generator
    pass_length: int = cli.get_number("Enter words count in password: ", max_=16)

    sep_symbol: str = input("Enter separation symbol: ")

    if not cli.yes_or_not("Will the password contain duplicate symbols?"):
        mode = "no_duplicate"

    passwords_count: int = cli.get_number("Enter count of passwords: ")

    # Password generation
    passwords: List[str] = [
        generate_password(pass_length, word_list, separator=sep_symbol, mode=mode) for _ in range(passwords_count)
    ]
    print("Your password is")
    for password in passwords:
        print(password)

    if cli.yes_or_not("Do you want to save passwords in file?"):
        file: str = input("Enter file name (default-\"passwords\"): ") or "password"
        save_to_file(file+".txt", passwords)


def config_pass() -> None:
    """Configures setting to generate password from symbols"""
    # Default alphabet
    raw_alphabet: str = string.ascii_lowercase
    # Default mode
    mode: str = "standard"

    # Config password generation
    pass_length: int = cli.get_number("Enter password length: ", max_=30)

    if cli.yes_or_not("Will the password contain capital letters?"):
        raw_alphabet += string.ascii_uppercase

    if cli.yes_or_not("Will the password contain digits?"):
        raw_alphabet += string.digits

    if cli.yes_or_not("Will the password contain special symbols?"):
        symbols: str = input("Enter special symbols: ")
        raw_alphabet += symbols

    if not cli.yes_or_not("Will the password contain duplicate symbols?"):
        mode = "no_duplicate"

    passwords_count: int = cli.get_number("Enter count of passwords: ")

    # Delete duplicate symbols
    alphabet: tuple = tuple(set(raw_alphabet))

    # Password generation
    passwords: List[str] = [
        generate_password(pass_length, alphabet, separator="", mode=mode) for _ in range(passwords_count)
    ]
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
