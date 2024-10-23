def backspaceCompare(s: str, t: str) -> bool:

    def next_valid_char_index(string, index):
        skip = 0
        while index >= 0:
            if string[index] == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                break
            index -= 1
        return index

    p1 = len(s) - 1
    p2 = len(t) - 1

    while p1 >= 0 or p2 >= 0:
        # find the next valid character for both strings
        p1 = next_valid_char_index(s, p1)
        p2 = next_valid_char_index(t, p2)

        if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
            return False

        if (p1 >= 0) != (p2 >= 0):
            return False

        p1 -= 1
        p2 -= 1

    return True


s = "ab#c"
t = "ad#c"

print(backspaceCompare(s, t))


# 5885bbbe-3847-4a92-af38-3a1898d2b5ff
