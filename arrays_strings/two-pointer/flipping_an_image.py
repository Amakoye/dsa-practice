from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:

    for i in range(len(image)):
        current_row = image[i]
        left = 0
        right = len(current_row) - 1

        # flip the image horizontally
        while left < right:
            temp = current_row[left]
            current_row[left] = current_row[right]
            current_row[right] = temp

            left += 1
            right -= 1

        #  invert the image
        for j in range(len(current_row)):
            if current_row[j] == 0:
                current_row[j] = 1

            elif current_row[j] == 1:
                current_row[j] = 0

    return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

print(flipAndInvertImage(image))
