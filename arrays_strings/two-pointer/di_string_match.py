from typing import List


def diStringMatch(s: str) -> List[int]:
    pointer1 = 0
    pointer2 = len(s)
    perm = []

    for i in range(len(s)):
        if s[i] == "I":
            perm.append(pointer1)
            pointer1 += 1

        else:
            perm.append(pointer2)
            pointer2 -= 1

    perm.append(pointer2)

    return perm


s = "IDID"
# s = "III"
print(diStringMatch(s))
