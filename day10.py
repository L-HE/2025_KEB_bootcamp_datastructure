import time
import random
import copy


def time_decorator(func):
    """
    td
    """
    def wrapper(*arg):
        """
        wrapper
        """
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'duration time: {e - s}sec')
        return r
    return  wrapper

@time_decorator
def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        while i > 0 and list[i - 1] > value:
            list[i] = list[i - 1]
            i -= 1
            #print(i, end=' ')
        list[i] = value
    return list

@time_decorator
def bubble_sort(list):
    count = 0
    for i in range(len(list) - 1):
        no_swaps = True
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swaps = False
            count += 1
            #print(j, end=' ')
        if no_swaps:
            return list
    print(f"\n{count}")


lists1 = [random.randint(1, 100000) for _ in range(10000)]
lists2 = lists1.copy()
print(insertion_sort(lists1))
print(bubble_sort(lists2))