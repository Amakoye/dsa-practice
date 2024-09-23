def convertToAnyNumber(n, b):
    nums = []

    while n > 0:
        nums.append(str(n % b))
        n //= b

    left = 0
    right = len(nums) - 1

    print(nums)

    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    print(nums)
    return "".join(nums)


def isStrictlyPalindromic(n: int) -> bool:
    for base in range(2, n - 1):
        # create the string respresentation of the number at this base
        num = n
        nums = []
        # Repeatedly divide n by base and keep track of remainders
        while num > 0:
            nums.append(str(num % base))
            num //= base

        # Build the number backwards from the remainders
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        string_num = "".join(nums)
        # check if the string is a palindrome
        p1 = 0
        p2 = len(string_num) - 1

        while p1 < p2:
            if string_num[p1] != string_num[p2]:
                #  Do nothing to is_palindrome
                return False

            p1 += 1
            p2 -= 1

    return True
