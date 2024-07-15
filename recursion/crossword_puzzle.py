def crosswordPuzzle(crossword, words):
    words_list = words.split(";")

    def is_valid_horizontal(crossword, word, row, col):
        if col + len(word) > 10:
            return False

        for i in range(len(word)):
            if crossword[row][col + i] != "-" and crossword[row][col + i] != word[i]:
                return False
        return True

    def place_word_horizontal(crossword, word, row, col):
        original = crossword[row][col : col + len(word)]
        crossword[row][col : col + len(word)] = list(word)
        return original

    def remove_word_horizontal(crossword, original, row, col):
        crossword[row][col : col + len(original)] = original

    def is_valid_vertical(crossword, word, row, col):
        if row + len(word) > 10:
            return False

        for i in range(len(word)):
            if crossword[row + i][col] != "-" and crossword[row + i][col] != word[i]:
                return False

        return True

    def place_word_vertical(crossword, word, row, col):
        original = [crossword[row + i][col] for i in range(len(word))]
        for i in range(len(word)):
            crossword[row + i][col] = word[i]
        return original

    def remove_word_vertical(crossword, original, row, col):
        for i in range(len(original)):
            crossword[row + i][col] = original[i]

    def solve(crossword, words_list):
        if not words_list:
            return True

        word = words_list.pop()

        for i in range(10):
            for j in range(10):
                if is_valid_horizontal(crossword, word, i, j):
                    original = place_word_horizontal(crossword, word, i, j)
                    if solve(crossword, words_list):
                        return True
                    remove_word_horizontal(crossword, original, i, j)

                if is_valid_vertical(crossword, word, i, j):
                    original = place_word_vertical(crossword, word, i, j)
                    if solve(crossword, words_list):
                        return True
                    remove_word_vertical(crossword, original, i, j)

        words_list.append(word)
        return False

    crossword = [list(row) for row in crossword]
    solve(crossword, words_list)
    return ["".join(row) for row in crossword]


crossword = [
    "++++++++++",
    "+------+++",
    "+++-++++++",
    "+++-++++++",
    "+++-----++",
    "+++-++-+++",
    "++++++-+++",
    "++++++-+++",
    "++++++-+++",
    "++++++++++",
]
words = "POLAND;LHASA;SPAIN;INDIA"
result = crosswordPuzzle(crossword, words)
for line in result:
    print(line)
