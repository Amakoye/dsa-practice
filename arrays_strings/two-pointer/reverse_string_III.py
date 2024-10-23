def reverseWords(s: str) -> str:
    list_words = s.split()

    for i in range(len(list_words)):
        char = list(list_words[i])
        left = 0
        right = len(char) - 1

        while left < right:
            temp = char[left]
            char[left] = char[right]
            char[right] = temp
            left += 1
            right -= 1

        list_words[i] = "".join(char)

    return " ".join(list_words)


# s = "Let's take LeetCode contest"

s = "Mr Ding"


print(reverseWords(s))
