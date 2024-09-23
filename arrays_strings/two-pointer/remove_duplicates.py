from typing import List


def removeDuplicates(nums: List[int]) -> int:

    pointer1 = 0

    for pointer2 in range(1, len(nums)):
        if nums[pointer2] != nums[pointer1]:
            pointer1 += 1
            nums[pointer1] = nums[pointer2]

    return pointer1 + 1


# nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
