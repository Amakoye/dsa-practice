def countBinarySubstrings(s: str) -> int:
    # Variables to track previous and current group lengths
    prev_count = 0  # Length of the previous group (either 0's or 1's)
    curr_count = 1  # Length of the current group (either 0's or 1's)
    result = 0  # To store the number of valid substrings

    # Loop through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # If current character is the same as previous, increase the current group count
            curr_count += 1
        else:
            # If there's a transition from 0 to 1 or 1 to 0
            result += min(
                prev_count, curr_count
            )  # Add smaller of the two group sizes to the result
            prev_count = (
                curr_count  # Update previous group size to the current group size
            )
            curr_count = 1  # Reset current group count for the new group

    # After the loop, there's one last comparison to make for the last two groups
    result += min(prev_count, curr_count)

    return result
