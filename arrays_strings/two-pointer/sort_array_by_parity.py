from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1

    nums.sort()

    while left < right:
        if nums[left] % 2 == 0:
            # do nothing and move left to right one step
            left += 1

        else:
            if nums[right] % 2 == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
            else:
                right -= 1

    return nums


nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))
