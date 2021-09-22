import string
import secrets

from utils import cli


def generate_password(length: int = 8, alphabet: str = string.ascii_letters + string.digits + "!?_-") -> str:
    return ''.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    pass_length = cli.get_number()
    print(generate_password(pass_length))
    input()
