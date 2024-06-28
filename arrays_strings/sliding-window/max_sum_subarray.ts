function maxSumSubArray(arr: number[], k: number): number {
  const n = arr.length;

  // check for the edge case
  if (n < k) {
    return -1;
  }

  let windowSum = 0;

  // calculate initial window sum for k
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }

  let maxSum = windowSum;

  // slide the window to the right
  for (let i = k; i < n; i++) {
    windowSum += arr[i] - arr[i - k];
    if (maxSum < windowSum) {
      maxSum = windowSum;
    }
  }

  return maxSum;
}

const arr_num: number[] = [2, 1, 5, 1, 3, 2];
const k: number = 3;
console.log(maxSumSubArray(arr_num, k));
