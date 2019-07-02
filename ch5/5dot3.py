def reverse_bits(w):
    
    res = 0
    copy_w = w
    for i in range(0, 8):
        
        res += tmp * (2^i - 1)

    return res

assert reverse_bits(73) == 146
assert reverse_bits(146) == 73
assert reverse_bits(8) == 16
assert reverse_bits(16) == 8

