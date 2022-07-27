import random

spisok = [random.randint(1, 15) for _ in range(15)]
numbers = [1, 2, 4, 5, 6, 9, 15, 21, 45, 56]


def binary_search(element, numbers):
    first = 0
    last = len(numbers)
    result = False
    while first < last:
        mid = (first + last) // 2

        if element == numbers[mid]:
            last = first
            result = True
            pos = mid
            return mid
        if element > numbers[mid]:
            first = mid + 1
        if element < numbers[mid]:
            last = mid - 1
    return -1


element = 45

print(f'Find {element}, in {numbers}')
print(f'Index {element} is {binary_search(element, numbers)}')


def bubble_sort(houses):
    ind = len(houses)

    for num in range(ind - 1):
        for j in range(0, ind - num - 1):
            if houses[j] > houses[j + 1]:
                houses[j], houses[j + 1] = houses[j + 1], houses[j]
    return houses


bubble_sort(spisok)
print(f'bubble sort{spisok}')



