def isSubsequence(s: str, t: str) -> bool:
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(s) and pointer2 < len(t):
        if s[pointer1] == t[pointer2]:
            pointer1 += 1
            pointer2 += 1
        else:
            pointer2 += 1

    return pointer1 == len(s)


# s = "abc"
# t = "ahbgdc"

s = "axc"
t = "ahbgdc"

print(isSubsequence(s, t))
