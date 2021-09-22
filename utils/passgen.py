import string
import secrets


class PasswordGenerator:
    def __init__(self, length: int = 8, alphabet: str = string.ascii_letters + string.digits + "!?_-"):
        self.length: int = length
        self.alphabet: str = alphabet

    def set_alphabet(self, symbols: str):
        self.alphabet = symbols

    def generate_password(self) -> str:
        return ''.join(secrets.choice(self.alphabet) for i in range(self.length))
