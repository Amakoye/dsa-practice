def find_pair_with_sum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return (arr[left], arr[right])
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


arr = [1, 2, 3, 4, 6]
target_sum = 6
print(find_pair_with_sum(arr, target_sum))
