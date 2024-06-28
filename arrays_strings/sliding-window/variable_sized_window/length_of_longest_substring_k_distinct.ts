/**
 * Problem: Longest Substring with At Most K Distinct Characters
 * Description: Given a string s and an integer k, find the length
 * of the longest substring that contains at most k distinct characters.
 *
 * Input: s = "eceba", k = 2
 * Output: 3
 * Explanation: The longest substring with at most 2 distinct characters is "ece".
 */

function lengthOfLongestSubstringKDistinct(s: string, k: number): number {
  let n = s.length;
  let left = 0;
  let right = 0;
  let maxLength = 0;
  let charSet = new Set<string>();

  while (right < n) {
    if (!charSet.has(s[right])) {
      charSet.add(s[right]);
      if (maxLength < right - left) {
        maxLength = right - left;
      }
      right++;
    } else {
      charSet.delete(s[left]);
      left++;
    }
  }

  return maxLength;
}

console.log(lengthOfLongestSubstringKDistinct("eceba", 2));

// correct implementation
function lengthOfLongestSubstringKDistinctCorrrect(
  s: string,
  k: number
): number {
  let n = s.length;
  if (k === 0 || n === 0) return 0;

  let left = 0;
  let right = 0;
  let maxLength = 0;
  let charMap: { [key: string]: number } = {};

  while (right < n) {
    // Add current character to the map and update its count
    let currentChar = s[right];
    charMap[currentChar] = (charMap[currentChar] || 0) + 1;

    // While the number of distinct characters in charMap is greater than k
    while (Object.keys(charMap).length > k) {
      let leftChar = s[left];
      charMap[leftChar]--;
      if (charMap[leftChar] === 0) {
        delete charMap[leftChar];
      }
      left++;
    }

    // Update maxLength if the current window size is larger
    maxLength = Math.max(maxLength, right - left + 1);
    right++;
  }

  return maxLength;
}

// Example usage:
console.log(lengthOfLongestSubstringKDistinctCorrrect("eceba", 2)); // Output: 3
