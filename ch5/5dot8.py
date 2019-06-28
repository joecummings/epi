def reverse_digits(x):
    reversed_str = str(x)[::-1]
    tail_i = len(reversed_str)-1
    if reversed_str[tail_i] == "-":
        return int("-"+reversed_str[:tail_i])
    return int(reversed_str)

def better_reverse_digits(x):
    return better_rd_helper(abs(x), 0)

def better_rd_helper(x, res):
    if res == 0:
        return res
    return better_rd_helper(x / 10, res * 10 + x % 10)

assert reverse_digits(45) == 54
assert reverse_digits(1) == 1
assert reverse_digits(-100) == -1

assert better_reverse_digits(45) == 54
assert better_reverse_digits(1) == 1
assert better_reverse_digits(-100) == -1
