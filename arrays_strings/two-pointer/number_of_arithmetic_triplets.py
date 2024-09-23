from typing import List


def arithmeticTriplets1(nums: List[int], diff: int) -> int:
    count = 0

    for index in range(len(nums)):
        _count = 0
        left = index
        right = index + 1

        while right < len(nums):
            _diff = nums[right] - nums[left]

            if _diff > diff:
                break

            if _diff == diff:
                _count += 1
                left = right
            if _count == 2:
                count += 1
                break
            right += 1

    return count


def arithmeticTriplets(nums: List[int], diff: int) -> int:
    count = 0

    for i in range(len(nums)):
        j = i + 1
        k = i + 2

        while j < len(nums) and k < len(nums):
            if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                count += 1
                break

            elif nums[j] - nums[i] < diff:
                j += 1
            elif nums[k] - nums[j] < diff:
                k += 1
            else:
                break

    return count


nums = [0, 1, 4, 6, 7, 10]
diff = 3

print(arithmeticTriplets(nums, diff))
