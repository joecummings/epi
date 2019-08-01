def mult_arbitrary_prec(num1: list, num2: list) -> list:

    l1 = [
        [0, 0, 0],
        [0, 0, 0]
        ]
    for i in range(0, len(num1)):
        for j in range(0, len(num2)):
            l1[i][j+i] = num1[i] * num2[j]
    
    return [sum(x) for x in zip(*l1)]

assert mult_arbitrary_prec([1,4], [1,1]) == [1,5,4]
