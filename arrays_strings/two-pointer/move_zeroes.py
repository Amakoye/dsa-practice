from typing import List


# def moveZeroes(nums: List[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """

#     left = 0

#     for right in range(1, len(nums)):
#         if nums[left] == 0 and nums[left] != nums[right]:
#             nums[left] = nums[right]
#             nums[right] = 0
#             left += 1
#         left += 1


#     print(nums)
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1

    print(nums)


nums = [1, 0, 1]
# nums = [0]
# nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
