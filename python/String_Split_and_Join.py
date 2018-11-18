def split_and_join(line):
    string_list = line.split(" ")
    hyphen_string = "-".join(string_list)
    return hyphen_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
