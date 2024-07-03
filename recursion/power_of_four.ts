function isPowerOfFour(n: number): boolean {
  if (n === 1) {
    return true;
  }
  if (n === 0 || n % 4 !== 0) {
    return false;
  }
  return isPowerOfFour(Math.floor(n / 4));
}

console.log(isPowerOfFour(16));
