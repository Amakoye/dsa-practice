function reverseWords(s: string): string {
  let split_str = s.trim().split(" ");
  let reverseArray: string[] = [];

  for (let i = 0; i < split_str.length; i++) {
    reverseArray[i] = split_str[split_str.length - i - 1];
  }

  return reverseArray.join(" ");
}

function reverseWords2(s: string): string {
  let split_str = s.trim().split(" ");
  let reverseArray: string[] = [];

  let p1 = 0;
  let p2 = split_str.length - 1;

  while (p1 >= 0 && p2 >= 0) {
    if (split_str[p2].length > 0) {
      reverseArray[p1] = split_str[p2];
      p1++;
    }
    p2--;
  }

  return reverseArray.join(" ");
}

console.log(reverseWords2("a good   example"));
