function lengthOfLongestSubstring(s: string): number {
  /**
   * Given a string 's', find the length of the longest substring without repeating characters
   * input s = "abcabcbb"
   * output = 3
   *
   * Approach
   * 1. use two pointers
   * use a sliding window with two pointers to represent the current window. One pointer ('left')
   * to denote the start of the window, and the other ('right') to denote the end.
   *
   * 2. Expand and contract the window
   * Expand the window by moving the right pointer to include more characters
   * If a character is repeated within the window, move the left pointer to reduce the window size
   * until the character is no longer repeated
   *
   * 3. Use a HashSet
   * Use a hashset to track characters in the current window to quickly check for repeats
   *
   */

  // implementation
  let n = s.length;
  let left = 0;
  let right = 0;
  let maxLength = 0;
  let charSet = new Set<string>();

  while (right < n) {
    if (!charSet.has(s[right])) {
      charSet.add(s[right]);

      if (maxLength < right - left + 1) {
        maxLength = right - left + 1;
      }
      right++;
    } else {
      charSet.delete(s[left]);
      left++;
    }
  }
  return maxLength;
}

/**
 * EXPLANATION
 * 1. Initialization
 * Initialize left and right pointers to 0, maxLength to 0 and an empty charset to store characters in
 * the current window
 *
 * 2. Expand the window
 * Move the right pointer to expand the window. if the character at right is not in charset, add it and
 * update maxLength
 *
 * 3. Contract the window
 * If the character at right is already in charset, move the left pointer to reduce the window size until
 * the duplicate is removed
 */

console.log(lengthOfLongestSubstring("abcabcbb"));
