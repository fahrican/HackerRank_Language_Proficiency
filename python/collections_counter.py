from collections import Counter

"""
collections.Counter() 
"""

if __name__ == '__main__':
    number_of_shoes = int(input())
    size_of_shoes = list(map(int, input().split(" ")))
    number_of_customers = int(input())
    earnings = 0
    counter_shoe_sizes = Counter(size_of_shoes)
    for i in range(number_of_customers):
        key_value = list(map(int, input().split(" ")))
        if counter_shoe_sizes[key_value[0]]:
            earnings += key_value[1]
            counter_shoe_sizes[key_value[0]] -= 1
    print(earnings)
