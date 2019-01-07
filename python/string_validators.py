"""
String Validators
"""


def string_validator(given_string: str):
    print(any(char.isalnum() for char in given_string))
    print(any(char.isalpha() for char in given_string))
    print(any(char.isdigit() for char in given_string))
    print(any(not char.isdigit() and char.isalpha() and char.islower() for char in given_string))
    print(any(not char.isdigit() and char.isalpha() and char.isupper() for char in given_string))


if __name__ == '__main__':
    given_string = input()
    string_validator(given_string)
