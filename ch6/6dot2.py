def inc_int(lod: list) -> list:
    return inc_helper(lod, len(lod)-1, False)


def inc_helper(lod: list, pos: int, carry: bool) -> list:
    if pos == 0:
        if not carry:
            return lod
        lod[0] += 1
        return lod

    if carry:
        lod[pos] += 1
        if is_ten(lod[pos]):
            lod[pos] = 0
            return inc_helper(lod, pos-1, True)
        return inc_helper(lod, 0, False)

    lod[pos] += 1
    if is_ten(lod[pos]):
        lod[pos] = 0
        return inc_helper(lod, pos - 1, True)

    return inc_helper(lod, 0, False)


def is_ten(num: int) -> bool:
    return num == 10


assert inc_int([1, 2, 9]) == [1, 3, 0]
assert inc_int([0, 0, 1]) == [0, 0, 2]
assert inc_int([1, 9, 9]) == [2, 0, 0]
