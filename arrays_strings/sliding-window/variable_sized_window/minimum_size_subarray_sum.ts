function minSubArrayLen(s: number, nums: number[]): number {
  /**
   * Given array of positive integers nums and a positive interger s, find the minimum length of
   * a contiguous subarray of which sum is greater than or equal to s. if there isn't one return 0
   */

  // implementation
  let n = nums.length;
  let left = 0;
  let right = 0;
  let sum = 0;

  let minLength = Infinity;

  while (right < n) {
    sum += nums[right];
    right++;

    while (sum >= s) {
      if (minLength > right - left) {
        sum -= nums[left];
        left++;
      }
    }
  }

  return minLength === Infinity ? 0 : minLength;
}

/**
 * EXPLANATION
 *
 * 1. Initialization
 * Left and right pointer both start at 0, and sum keeps track of the sum of the current window
 *
 * 2. Expand window
 * Move the right pointer to include more elements and increase the sum
 *
 * 3. Contract window
 * If the sum is greater than or equal to s, update the minimum length and move the left pointer to reduce the sum and shrink the window
 */
