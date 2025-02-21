def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        while i > 0 and list[i - 1] > value:
            list[i] = list[i - 1]
            i -= 1
            print(i, end=' ')
        list[i] = value
    return list


def bubble_sort(list):
    count = 0
    for i in range(len(list) - 1):
        no_swaps = True
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swaps = False
            count += 1
            print(j, end=' ')
        if no_swaps:
            return list
    print(f"\n{count}")


print(bubble_sort([8, -11, 91, 35, 10])
print(insertion_sort([8, -11, 91, 35, 10]))