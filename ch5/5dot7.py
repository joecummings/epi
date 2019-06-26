def exponential(base, exp):
    if exp < 1:
        return 1
    if exp == 1:
        return base
    return exponential(base+base, exp-1)

def faster_exponential(base, exp):
    res = 1
    power = exp
    if exp < 0:
        power = -power
        base = 1/base
    while power:
        if power & 1:
            res *= base
        base *= base
        power >>= 1
    return res


assert exponential(2,1) == 2
assert exponential(2,0) == 1
assert exponential(2,3) == 8
assert exponential(2,8) == 256

assert faster_exponential(2,1) == 2
assert faster_exponential(2,0) == 1
assert faster_exponential(2,3) == 8
assert faster_exponential(2,8) == 256

