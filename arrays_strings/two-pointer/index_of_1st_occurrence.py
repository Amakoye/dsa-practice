def strStr(haystack: str, needle: str) -> int:
    # Approach 1
    # for i in range(len(haystack)):
    #     if haystack[i : i + len(needle)] == needle:
    #         return i
    # return -1

    # if not needle:
    #     return 0  # Edge case: if needle is an empty string, return 0

    # for i in range(len(haystack) - len(needle) + 1):  # Adjust loop to stop early
    #     if haystack[i : i + len(needle)] == needle:
    #         return i
    # return -1

    # Approach 2

    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            else:
                return i

    return -1


haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))
