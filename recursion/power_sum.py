def powerSum(X, N):
    def powerSumHelper(X, N, current_num):
        if X == 0:
            return 1  # found a valid way to sum to 0

        if X < 0:
            return 0  # Overshot, no valid way

        ways = 0
        start = current_num

        while True:
            power = start**N

            if power > X:
                break
            ways += powerSumHelper(X - power, N, start + 1)
            start += 1

        return ways

    # Start recursion from X, with N-th powers starting from 1
    return powerSumHelper(X, N, 1)


print(powerSum(13, 2))
