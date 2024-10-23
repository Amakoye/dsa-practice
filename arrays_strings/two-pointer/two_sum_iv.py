from typing import Optional


def findTarget(root, k: int) -> bool:  # type: ignore

    left = 0

    for right in range(left + 1, len(root)):
        if type(root[left]) == int and type(root[right]) == int:
            _sum = root[left] + root[right]

            if _sum == k:
                return True

            left += 1

    return False


root = [5, 3, 6, 2, 4, 7]
k = 28

print(findTarget(root, k))

# for left in range(len(root)):
#     right = left + 1

#     _sum =

#     if _sum == k:
#         return True
