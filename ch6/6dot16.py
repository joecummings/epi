def soduku_checker(arr: list) -> bool:

    target = 45
    for i in range(0, len(arr)-1):
        col_sum = 0
        if sum(arr[i]) != target or set(arr[i]) < 9:
            return False

    return True

x = [
    [1,2,3],
    [2,3,1],
    [3,1,2]
]   
