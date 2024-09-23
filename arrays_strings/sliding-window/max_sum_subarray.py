def maxSumSubArray(nums, k):
    n = len(nums)
    window_sum = 0
    max_sum = 0

    if n < k:
        return -1

    # calculate the sum of first window size K
    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    # slide the window from start to the end of the array

    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3

print(maxSumSubArray(nums, k))
