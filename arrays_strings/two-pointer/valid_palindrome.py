def isPalindrome(s: str) -> bool:
    stripped_str = "".join(filter(str.isalnum, s)).lower()
    # stripped_str = (
    #     s.strip(" ").replace(" ", "").replace(",", "").replace(":", "").lower()
    # )
    left = 0
    right = len(stripped_str) - 1

    print(stripped_str)
    while left < right:
        if stripped_str[left] != stripped_str[right]:
            return False
        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
# s = "race a car"
print(isPalindrome(s))
