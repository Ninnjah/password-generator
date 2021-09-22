def get_number():
    while True:
        try:
            return int(input("Enter password length: "))
        except ValueError:
            print("You should enter a number")
