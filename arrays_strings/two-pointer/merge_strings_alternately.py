def mergeAlternately(word1: str, word2: str) -> str:
    word_list = []
    pointer_1 = 0
    pointer_2 = 0

    while pointer_1 < len(word1) and pointer_2 < len(word2):

        word_list.append(word1[pointer_1])
        word_list.append(word2[pointer_2])
        pointer_1 += 1
        pointer_2 += 1

    if pointer_1 < len(word1):
        word_list.append(word1[pointer_1:])

    if pointer_2 < len(word2):
        word_list.append(word2[pointer_2:])

    return "".join(word_list)


# word1 = "abc"
# word2 = "pqr"

word1 = "ab"
word2 = "pqrs"


print(mergeAlternately(word1, word2))
