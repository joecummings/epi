import math

def is_palindrome(x: int )-> bool:
    str_x = str(x)
    if str_x[::-1] == str_x:
        return True
    return False

def better_is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    if x < 10:
        return True

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = math.pow(10, num_digits - 1)
    for i in range(math.ceil(num_digits/2)):
        if (int(x / msd_mask) != int(x % 10)):
            return False
        
        x %= 10 # remove msd
        x /= 10 # remove lsd
        msd_mask /= 100
       
    return True

assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(1) == True

assert better_is_palindrome(121) == True
assert better_is_palindrome(123) == False
assert better_is_palindrome(1) == True