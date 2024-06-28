function maxAverageSubarray(arr: number[], k: number): number {
  const n = arr.length;

  if (n < k) {
    return -1;
  }

  let window_average = 0;
  let window_sum = 0;

  for (let i = 0; i < k; i++) {
    window_sum += arr[i];
  }

  window_average = window_sum / k;

  let max_avarage = window_average;

  for (let i = k; i < n; i++) {
    window_sum += arr[i] - arr[i - k];
    window_average = window_sum / k;

    if (window_average > max_avarage) {
      max_avarage = window_average;
    }
  }

  return max_avarage;
}

function minSumSubarray(arr: number[], k: number): number {
  let n = arr.length;

  if (n < k) {
    return -1;
  }

  let window_sum = 0;

  for (let i = 0; i < k; i++) {
    window_sum += arr[i];
  }

  let min_sum = window_sum;

  for (let i = k; i < n; i++) {
    window_sum += arr[i] - arr[i - k];

    if (window_sum < min_sum) {
      min_sum = window_sum;
    }
  }

  return min_sum;
}

function maxSumSubArray(arr: number[], k: number) {
  let n = arr.length;

  if (n < k) {
    return -1;
  }

  let window_sum = 0;

  for (let i = 0; i < k; i++) {
    window_sum += arr[i];
  }

  let max_sum = window_sum;

  for (let i = k; i < n; i++) {
    window_sum += arr[i] - arr[i - k];

    if (max_sum < window_sum) {
      max_sum = window_sum;
    }
  }

  return max_sum;
}

function firstNegativeNumber(arr: number[], k: number): number[] {
  let n = arr.length;

  if (n < k) {
    return [];
  }

  let negative_nums: number[] = [];
  let negative_indices: number[] = [];

  // Initialize the queue for the first window
  for (let i = 0; i < k; i++) {
    if (arr[i] < 0) {
      // negative_nums.push(arr[i]);
      negative_indices.push(i);
    }
  }

  // Process the first window result
  if (negative_indices.length > 0) {
    negative_nums.push(arr[negative_indices[0]]);
  } else {
    negative_nums.push(0);
  }

  // Slide the window across the array
  for (let i = k; i < n; i++) {
    // Remove indices that are out of the current window
    if (negative_indices.length > 0 && negative_indices[0] < i - k + 1) {
      negative_indices.shift();
    }

    // Add the current element index if it is negative
    if (arr[i] < 0) {
      negative_indices.push(i);
    }

    // Add the first negative number in the current window to the result
    if (negative_indices.length > 0) {
      negative_nums.push(arr[negative_indices[0]]);
    } else {
      negative_nums.push(0);
    }
  }

  return negative_nums;
}

function maxSubArray(arr: number[], k: number): number[] {
  let n = arr.length;

  if (n < k) {
    return [];
  }

  let max_elements: number[] = [];
  let max_indices: number[] = [];

  for (let i = 0; i < k; i++) {
    if (arr[i] > arr[i + 1]) {
      max_indices.push(i);
    } else {
      max_indices.push(i + 1);
    }
  }

  if (max_indices.length > 0) {
    max_elements.push(arr[max_indices[0]]);
  }

  for (let i = k; i < n; i++) {
    if (max_indices.length > 0 && max_indices[0] < i - k + 1) {
      max_indices.shift();
    }

    if (arr[i] > arr[i + 1]) {
      max_indices.push(i);
    } else {
      max_indices.push(i + 1);
    }

    if (max_indices.length > 0) {
      max_elements.push(arr[max_indices[0]]);
    }
  }

  return max_elements;
}

// const arr = [1, 12, -5, -6, 50, 3];
// const constraint = 4;

// console.log(maxAverageSubarray(arr, constraint));

// const arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0];
// const constraint = 3;
// console.log(minSumSubarray(arr, constraint));

// const arr = [2, 1, 5, 1, 3, 2];
// const k = 3;
// console.log(maxSumSubArray(arr, k));

// const arr2: number[] = [12, -1, -7, 8, -15, 30, 16, 28];
// const k2: number = 3;
// console.log(firstNegativeNumber(arr2, k2));

const arr = [1, 3, 1, 2, 0, 5];
const k = 3;
console.log(maxSubArray(arr, k));
