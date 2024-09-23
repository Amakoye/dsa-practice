from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    pointer1 = 0
    pointer2 = 0

    # intersection_list: List[int] = []
    intersection_set = set()

    while pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] == nums2[pointer2]:
            # intersection_list.append(nums1[pointer1])
            intersection_set.add(nums1[pointer1])
            pointer1 += 1
            pointer2 += 1

        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1

    return list(intersection_set)


def intersectionII(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    pointer1 = 0
    pointer2 = 0

    intersection_list: List[int] = []

    while pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] == nums2[pointer2]:
            intersection_list.append(nums1[pointer1])
            pointer1 += 1
            pointer2 += 1

        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1

    return intersection_list


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

print(intersectionII(nums1, nums2))
