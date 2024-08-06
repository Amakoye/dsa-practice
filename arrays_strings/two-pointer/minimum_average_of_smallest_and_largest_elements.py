from typing import List


def solution(nums: List[int]):

    nums.sort()
    n = len(nums)
    averages = []

    for i in range(int(n / 2)):
        minElement = nums.pop(0)
        maxElement = nums.pop()

        current_average = (minElement + maxElement) / 2
        averages.append(current_average)

    averages.sort()
    minAverage = averages[0]

    return minAverage


# nums = [7, 8, 3, 4, 15, 13, 4, 1]
# nums = [1, 2, 3, 7, 8, 9]
nums = [1, 9, 8, 3, 10, 5]
solution(nums)
