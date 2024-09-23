from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    MAX_NUMBER = 0

    pointer1 = 0
    pointer2 = 0

    g.sort()
    s.sort()

    while pointer1 < len(g) and pointer2 < len(s):
        if s[pointer2] >= g[pointer1]:
            MAX_NUMBER += 1
            pointer1 += 1
            pointer2 += 1
        else:
            pointer2 += 1

    return MAX_NUMBER


# g = [1, 2, 3]
# s = [1, 1]

# g = [1, 2]
# s = [1, 2, 3]


# g = [1, 2, 3]
# s = [3]

g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(findContentChildren(g, s))
