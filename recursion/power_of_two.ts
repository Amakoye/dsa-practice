function isPowerOfTwo(n: number): boolean {
  if (n === 1) {
    return true;
  }
  if (n == 0 || n % 2 !== 0) {
    return false;
  }

  return isPowerOfTwo(Math.floor(n / 2));
}
