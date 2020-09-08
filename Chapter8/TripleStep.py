def triple_step_recursion(n):
    if n < 0: return 0
    elif n == 0: return 1
    else:
        return triple_step_recursion(n-1) + triple_step_recursion(n-2) + triple_step_recursion(n-3)


# Top Down
def triple_step_dp(n):
    return _helper(n, [-1] * (n+1))


def _helper(n, cache):
    if n < 0: return 0
    elif n == 0: return 1
    elif cache[n] > -1:
        return cache[n]
    else:
        cache[n] = _helper(n-3, cache) + _helper(n-2, cache) + _helper(n-1, cache)
        return cache[n]


# Bottom Up
def triple_step_dp_bu(n):
    cache = [0] * (n+1)
    cache[0], cache[1], cache[2] = 1, 1, 2

    for i in range(3, n+1):
        cache[i] = cache[i-3] + cache[i-2] + cache[i-1]
    return cache[n]


if __name__ == '__main__':
    # for n in range(20):
        # assert (triple_step_recursion(n)) == (triple_step_dp(n)) == triple_step_dp_bu(n)

    print(triple_step_recursion(20))
    print(triple_step_dp(20))
    print(triple_step_dp_bu(20))







