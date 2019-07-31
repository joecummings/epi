def delete_duplicates(sorted_arr: list) -> list:
    return delete_helper(sorted_arr[1:], sorted_arr[0])

def delete_helper(rest_arr: list, curr: int) -> list:
    if len(rest_arr) == 2:
        return rest_arr
    if rest_arr[0] == curr:
        return (delete_helper(rest_arr[1:], curr)
    return delete_helper(rest_arr[1:], rest_arr[2]).insert(0, rest_arr[0])

print(delete_duplicates([1,1,2,3,4]))
assert delete_duplicates([1,1,2,3,4]) == [1,2,3,4]
