from typing import List


def firstPalindrome(words: List[str]) -> str:
    for i in range(len(words)):
        currentWordArr = list(words[i])
        left = 0
        right = len(currentWordArr) - 1

        while left < right:
            temp = currentWordArr[left]
            currentWordArr[left] = currentWordArr[right]
            currentWordArr[right] = temp
            left += 1
            right -= 1

        reversedWord = "".join(currentWordArr)

        if words[i] == reversedWord:
            return words[i]

    return ""


def solution2(words: List[str]) -> str:
    for word in words:
        left = 0
        right = len(word) - 1
        is_palindrome = True

        while left < right:
            if word[left] != word[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1

        if is_palindrome:
            return word

    return ""


# words = ["abc", "car", "ada", "racecar", "cool"]

words = ["notapalindrome", "racecar"]

print(solution2(words))
