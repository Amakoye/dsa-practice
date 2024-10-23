from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    n = len(s)
    answer = [float("inf")] * n
    prev_c_index = -float("inf")

    for i in range(n):
        if s[i] == c:
            prev_c_index = i
        answer[i] = abs(i - prev_c_index)

    prev_c_index = float("inf")
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev_c_index = i
        answer[i] = min(answer[i], abs(i - prev_c_index))

    return answer


s = "aaab"
c = "b"

# s = "loveleetcode"
# c = "e"

print(shortestToChar(s, c))
