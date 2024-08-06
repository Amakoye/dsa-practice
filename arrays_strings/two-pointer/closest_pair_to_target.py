def closest_pair_to_target(arr, target):
    left, right = 0, len(arr) - 1
    closest_pair = (arr[left], arr[right])
    closest_sum = arr[left] + arr[right]

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return closest_pair


arr = [1, 3, 4, 7, 10]
target = 15
print(closest_pair_to_target(arr, target))
