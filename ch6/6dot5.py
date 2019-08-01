def delete_duplicates(sorted_arr: list) -> list:
    
    if len(sorted_arr) == 0:
        return 0
    
    curr = 1

    for i in range(1, len(sorted_arr)-1):
        if sorted_arr[curr - 1] != sorted_arr[i]:
            curr += 1
            sorted_arr[curr] = sorted_arr[i] 

    return curr

assert delete_duplicates([2,3,5,5,7,11,11,11,13]) == 6
