from collections import Counter

"""
collections.Counter() 
"""

if __name__ == '__main__':
    number_of_shoes = int(input())
    size_of_shoes = list(map(int, input().split(' ')))
    counter_shoe_sizes = Counter(size_of_shoes)
    number_of_customers = int(input())
    earnings = 0
    for i in range(number_of_customers):
        size, price = map(int, input().split(' '))
        if counter_shoe_sizes[size]:
            earnings += price
            counter_shoe_sizes[size] -= 1
    print(earnings)
