import numpy as np
import math

def spiral_ordering(arr: list) -> list:
    lens = len(arr)
    trans = np.asarray(arr).T

    ret = []

    for i in range(0, math.ceil(lens/2)):
        ret.append(arr[i][i*1:])

        ret.append(trans[lens-(i+1)][i+1:])

        ret.append(arr[lens-(i+1)][i+1::-1])

        ret.append(trans[i][lens-2:0:-1])

    return [item for sublist in ret for item in sublist]

def maxtrix_spiral_ordering(arr: list) -> list:
    pass

# [
#   [1 2 3]
#   [4 5 6]
#   [7 8 9] 
# ]

# [
#   [1 4 7]
#   [2 5 8]
#   [3 6 9]
# ]



# assert spiral_ordering([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]