def reversePrefix(word: str, ch: str) -> str:
    new_word = ""

    left = 0
    right = 0

    for i in range(len(word)):
        if word[right] == ch:
            prefix = list(word[left : right + 1])

            while left < right:
                temp = prefix[left]
                prefix[left] = prefix[right]
                prefix[right] = temp
                right -= 1
                left += 1

            new_word = "".join(prefix) + word[len(prefix) :]
            break
        else:
            right += 1
            new_word = word

    return new_word


word = "abcdefd"
ch = "d"

# word = "abcdefd"
# ch = "d"
# word = "abcd"
# ch = "z"

print(reversePrefix(word, ch))
