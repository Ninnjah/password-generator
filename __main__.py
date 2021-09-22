import string
import secrets


def generate_password(length: int = 8, alphabet: str = string.ascii_letters + string.digits + "!?_-") -> str:
    return ''.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    while True:
        try:
            pass_length = int(input("Enter password length: "))
            break
        except ValueError:
            print("You should enter a number")

    print(generate_password(pass_length))
    input()
