"""  
The idea is to repeatedly divide the number by 4 and check if you eventually get down to 1

If n is 1, it is a power of four.
If n is less than 1 or not divisible by 4, it is not a power of four.
Otherwise, recursively check if n/4 is a power of four.
"""


def isPowerOfFour(n):
    if n == 1:
        return True

    if n == 0 or n % 4 != 0:
        return False
    return isPowerOfFour(n // 4)


print(isPowerOfFour(16))
