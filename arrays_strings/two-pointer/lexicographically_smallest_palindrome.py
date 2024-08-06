def makeSmallestPalindrome(s: str) -> str:
    arr_str = list(s)

    left = 0
    right = len(arr_str) - 1

    while left < right:

        if arr_str[left] > arr_str[right]:
            arr_str[left] = arr_str[right]

        elif arr_str[right] > arr_str[left]:
            arr_str[right] = arr_str[left]

        left += 1
        right -= 1

    return "".join(arr_str)


# s = "egcfe"
# s = "abcd"
s = "seven"
print(makeSmallestPalindrome(s))
