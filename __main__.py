import string
import secrets

from utils import cli


def generate_password(length: int, alphabet: tuple) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    RAW_ALPHABET: str = string.ascii_lowercase

    pass_length = cli.get_number("Enter password length: ")

    if cli.yes_or_not("Will the password contain capital letters?"):
        RAW_ALPHABET += string.ascii_uppercase

    if cli.yes_or_not("Will the password contain digits?"):
        RAW_ALPHABET += string.digits

    if cli.yes_or_not("Will the password contain special symbols?"):
        symbols = input("Enter special symbols: ")
        RAW_ALPHABET += symbols

    ALPHABET: tuple = tuple(set(RAW_ALPHABET))

    print(generate_password(pass_length, ALPHABET))
    input()
