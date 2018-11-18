def swap_case(s):
    string_swap_case = ""
    for character in s:
        string_swap_case += character.swapcase()
    return string_swap_case


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
