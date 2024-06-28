function removeDuplicates(nums: number[]): number {
  let slowerPointer: number = 0;

  for (let fasterPointer = 1; fasterPointer < nums.length; fasterPointer++) {
    if (nums[fasterPointer] !== nums[slowerPointer]) {
      slowerPointer++;
      nums[slowerPointer] = nums[fasterPointer];
    }
  }

  console.log(nums.slice(0, slowerPointer + 1));
  return slowerPointer + 1;
}

function removeDuplicates2(nums: number[]): number {
  let unique_arr: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i + 1]) {
      unique_arr.push(nums[i]);
    } else {
    }
  }

  console.log(unique_arr);

  return 0;
}

console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));
