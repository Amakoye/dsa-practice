function removeDuplicates(nums: number[]): number {
  let slowerPointer: number = 2;

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] !== nums[slowerPointer - 2]) {
      nums[slowerPointer] = nums[i];
      slowerPointer++;
    }
  }

  nums.slice(0, slowerPointer);

  return slowerPointer;
}

console.log(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]));
