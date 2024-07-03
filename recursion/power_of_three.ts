/* 
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
*/

function isPowerOfThree(n: number): boolean {
  if (n === 1) {
    return true;
  }
  if (n == 0 || n % 3 !== 0) {
    return false;
  }

  return isPowerOfThree(Math.floor(n / 3));
}

console.log(isPowerOfThree(-1));
