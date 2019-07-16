from random import randint

def eq_subset(arr: list, size: int) -> list:
    for i in range(size):
       elem = randint(i, size)
       arr = swap(arr, i, elem)
    return arr[:size]

def swap(arr: list, first: int, second: int) -> list:
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr

print(eq_subset([3,7,5,11], 3))
        
