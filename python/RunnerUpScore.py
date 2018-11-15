if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = sorted(arr)
    biggest_number = max(my_list)
    i = (len(my_list) - 1)
    while i >= 0:
        if my_list[i] < biggest_number:
            print(my_list[i])
            break
        else:
            i -= 1
