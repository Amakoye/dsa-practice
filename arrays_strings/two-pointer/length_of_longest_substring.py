def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:

            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length


s = "abcabcbb"
print(length_of_longest_substring(s))
