def enum_all_primes(n: int) -> list:
    res = list()

    for i in range(2, n):
        for p in res:
            if n % p == 0:
                continue
        if is_prime(i):
            res.append(i)
    
    return res

def is_prime(n: int) -> bool:
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
        return True

assert enum_all_primes(18) == [2,3,5,7,11,13,17]