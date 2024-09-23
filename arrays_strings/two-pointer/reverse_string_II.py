def reverseStr(s: str, k: int) -> str:
    list_str = list(s)
    list_len = len(list_str)
    i = 0

    while i < list_len:

        left = i
        right = min(i + k - 1, list_len - 1)

        while left < right:
            list_str[left], list_str[right] = list_str[right], list_str[left]
            left += 1
            right -= 1

        i += 2 * k

    return "".join(list_str)


# s = "abcdefg"
# k = 2

s = "abcd"
k = 2

print(reverseStr(s, k))
