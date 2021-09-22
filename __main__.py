import string
import secrets

from utils import cli


def generate_password(length: int = 8, alphabet: str = string.ascii_letters + string.digits + "!?_-") -> str:
    return ''.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    ALPHABET: str = string.ascii_lowercase

    pass_length = cli.get_number()

    if cli.yes_or_not("Password will be have a capital letters?"):
        ALPHABET += string.ascii_uppercase

    if cli.yes_or_not("Password will be have a digits?"):
        ALPHABET += string.digits

    if cli.yes_or_not("Password will be have a other symbols?"):
        ALPHABET += "!?_-"

    print(generate_password(pass_length, ALPHABET))
    input()
