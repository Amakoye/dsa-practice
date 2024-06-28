function removeElement(nums: number[], val: number): number {
  let count: number = 0;
  let k: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      k.push(nums[i]);
    }
  }

  for (let i = 0; i < k.length; i++) {
    nums[i] = k[i];
  }

  return k.length;
}

// Two pointer approach (Pointers moving in the same direction)

function removeElement2(nums: number[], val: number): number {
  let count: number = 0; // slower pointer

  for (let i = 0; i < nums.length; i++) {
    // var i acts as our faster ponter
    if (nums[i] !== val) {
      nums[count] = nums[i];
      count++;
    }
  }

  return count;
}

console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2));
