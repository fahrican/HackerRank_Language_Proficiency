"""
String Validators
"""


def string_validator(given_string: str):
    if any(char.isalnum() for char in given_string):
        print('True')
    else:
        print('False')
    if any(char.isalpha() for char in given_string):
        print('True')
    else:
        print('False')
    if any(char.isdigit() for char in given_string):
        print('True')
    else:
        print('False')
    if any(char.islower() and char.isalpha() for char in given_string):
        print('True')
    else:
        print('False')
    if any(not char.isdigit() and char.isalpha() and char.isupper() for char in given_string):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    given_string = input()
    string_validator(given_string)
