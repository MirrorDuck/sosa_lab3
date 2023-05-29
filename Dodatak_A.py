import ast
import os
import getpass


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if self.b == 0:
            return float('nan')
        return self.a / self.b


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())

    expression = input('Enter a mathematical formula to calculate: ')
    try:
        result = ast.literal_eval(expression)
        print("Result:", result)
    except (ValueError, SyntaxError):
        print("Invalid mathematical expression!")


def main():
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if not authenticate(user, password):
        print("Wrong username or password!")
        exit(0)

    print("Login success!")
    login_success()


def authenticate(user, password):
    credentials_file = "credentials.txt"

    with open(credentials_file, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            if key.strip() == 'username' and user == value.strip():
                next_line = next(file, None)
                if next_line:
                    key, value = next_line.strip().split(':')
                    if key.strip() == 'password' and password == value.strip():
                        return True
    return False
