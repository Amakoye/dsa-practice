function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  // pointers for num1 and num2
  let p1 = m - 1;
  let p2 = n - 1;
  let p = m + n - 1;

  // merge elements from end
  while (p1 >= 0 && p2 >= 0) {
    if (nums1[p1] > nums2[p2]) {
      nums1[p] = nums1[p1];
      p1--;
    } else {
      nums1[p] = nums2[p2];
      p2--;
    }
    p--;
  }

  while (p2 >= 0) {
    nums1[p] = nums2[p2];
    p2--;
    p--;
  }
}

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3);
