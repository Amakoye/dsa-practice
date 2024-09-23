def reverseVowels(s: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]

    list_str = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        # if the char at left and right are both vowels then swap them, then increment left by 1 and decrement right by 1
        # if the char at left is not a vowel and char at right is a vowel increment left by 1,
        # if the char at right is not a vowel and char at left is a vowel decrement right by 1,
        if list_str[left].lower() not in vowels:
            left += 1
        elif list_str[right].lower() not in vowels:
            right -= 1
        else:
            temp = list_str[left]
            list_str[left] = list_str[right]
            list_str[right] = temp
            left += 1
            right -= 1

    return "".join(list_str)


# s = "IceCreAm"
s = "leetcode"
print(reverseVowels(s))
