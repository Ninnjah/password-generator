from utils.passgen import PasswordGenerator


if __name__ == "__main__":
    passgenerator = PasswordGenerator()
    print(passgenerator.generate_password())
