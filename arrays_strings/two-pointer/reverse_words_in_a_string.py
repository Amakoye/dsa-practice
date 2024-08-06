def reverseWords(s: str) -> str:
    words = s.split()

    for i in range(len(words)):

        left = 0
        right = len(words[i]) - 1
        split_word = list(words[i])

        while left < right:
            temp = split_word[left]
            split_word[left] = split_word[right]
            split_word[right] = temp
            left += 1
            right -= 1

        words[i] = "".join(split_word)

    return " ".join(words)


s = "Let's take LeetCode contest"

print(reverseWords(s))
