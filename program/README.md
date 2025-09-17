# 100 Most Common Coding Interview Programs (JavaScript)

Below are 100 easy to medium level programs frequently asked in coding interviews at companies like WIPRO, TCS, INFOSYS, ACCENTURE, CAPGEMINI, HCL TECH, TECH MAHINDRA, IBM, DELOITTE, COGNIZANT, etc. Each program includes a JavaScript solution.

---

1. **Reverse a String**
- **Explanation:** Reverses the characters in a string. Common for string manipulation and basic logic.
- **Input:** "hello"
- **Output:** "olleh"
- **Time Complexity:** O(n) — where n is the length of the string (split, reverse, join each take O(n)).
- **Space Complexity:** O(n) — new array is created for split/reverse/join.
```js
function reverseString(str) {
  return str.split('').reverse().join('');
}
```

2. **Check for Palindrome**
- **Explanation:** Checks if a string reads the same forwards and backwards. Palindrome checks are common in interviews.
- **Input:** "madam"
- **Output:** true
- **Time Complexity:** O(n) — string reversal is O(n).
- **Space Complexity:** O(n) — new reversed string is created.
```js
function isPalindrome(str) {
  return str === str.split('').reverse().join('');
}
```

3. **Find Factorial**
- **Explanation:** Calculates the factorial of a number. Used to test recursion and loops.
- **Input:** 5
- **Output:** 120
- **Time Complexity:** O(n) — n recursive calls.
- **Space Complexity:** O(n) — call stack for recursion.
```js
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}
```

4. **Find Fibonacci Number**
- **Explanation:** Returns the nth Fibonacci number. Used to test recursion and dynamic programming basics.
- **Input:** 6
- **Output:** 8
- **Time Complexity:** O(2^n) — exponential due to repeated subproblems (for this recursive version).
- **Space Complexity:** O(n) — call stack for recursion.
```js
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

5. **Find Largest Element in Array**
- **Explanation:** Finds the largest number in an array. Array traversal is a basic skill.
- **Input:** [1, 5, 2, 9, 3]
- **Output:** 9
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — only a variable for max is used.
```js
function largest(arr) {
  return Math.max(...arr);
}
```

6. **Find Smallest Element in Array**
- **Explanation:** Finds the smallest number in an array.
- **Input:** [1, 5, 2, 9, 3]
- **Output:** 1
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — only a variable for min is used.
```js
function smallest(arr) {
  return Math.min(...arr);
}
```

7. **Sum of Array Elements**
- **Explanation:** Sums all elements in an array. Used to test array methods and loops.
- **Input:** [1, 2, 3, 4]
- **Output:** 10
- **Time Complexity:** O(n) — reduce iterates through all elements.
- **Space Complexity:** O(1) — only an accumulator variable is used.
```js
function sumArray(arr) {
  return arr.reduce((a, b) => a + b, 0);
}
```

8. **Remove Duplicates from Array**
- **Explanation:** Removes duplicate values from an array. Set usage is a common topic.
- **Input:** [1, 2, 2, 3, 4, 4]
- **Output:** [1, 2, 3, 4]
- **Time Complexity:** O(n) — each element is processed once.
- **Space Complexity:** O(n) — new Set and array are created.
```js
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
```

9. **Check if Number is Prime**
- **Explanation:** Checks if a number is prime. Prime logic is a classic interview question.
- **Input:** 7
- **Output:** true
- **Time Complexity:** O(√n) — checks up to square root of n.
- **Space Complexity:** O(1) — uses a few variables.
```js
function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
```

10. **Print Prime Numbers in Range**
- **Explanation:** Returns all prime numbers up to n. Used to test loops and prime logic.
- **Input:** 10
- **Output:** [2, 3, 5, 7]
- **Time Complexity:** O(n√n) — for each number up to n, checks up to √n.
- **Space Complexity:** O(k) — where k is the number of primes found.
```js
function printPrimes(n) {
  let primes = [];
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) primes.push(i);
  }
  return primes;
}
```

11. **Find GCD of Two Numbers**
- **Explanation:** Finds the greatest common divisor (GCD) of two numbers. Used to test recursion and math logic.
- **Input:** 12, 18
- **Output:** 6
- **Time Complexity:** O(log(min(a, b))) — Euclidean algorithm.
- **Space Complexity:** O(log(min(a, b))) — recursion stack.
```js
function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}
```

12. **Find LCM of Two Numbers**
- **Explanation:** Finds the least common multiple (LCM) of two numbers. Often paired with GCD.
- **Input:** 4, 6
- **Output:** 12
- **Time Complexity:** O(log(min(a, b))) — depends on GCD.
- **Space Complexity:** O(1) — uses a few variables.
```js
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}
```

13. **Check Armstrong Number**
- **Explanation:** Checks if a number is an Armstrong number (sum of its own digits each raised to the power of the number of digits equals the number itself).
- **Input:** 153
- **Output:** true
- **Time Complexity:** O(d) — d is the number of digits in n.
- **Space Complexity:** O(1) — uses a few variables.
```js
function isArmstrong(n) {
  let sum = 0, temp = n;
  let digits = n.toString().length;
  while (temp > 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum === n;
}
```

14. **Check Perfect Number**
- **Explanation:** Checks if a number is perfect (sum of its divisors equals the number).
- **Input:** 28
- **Output:** true
- **Time Complexity:** O(n) — checks all numbers less than n.
- **Space Complexity:** O(1) — uses a few variables.
```js
function isPerfect(n) {
  let sum = 0;
  for (let i = 1; i < n; i++) {
    if (n % i === 0) sum += i;
  }
  return sum === n;
}
```

15. **Find Second Largest in Array**
- **Explanation:** Finds the second largest number in an array. Tests array traversal and logic.
- **Input:** [1, 5, 2, 9, 3]
- **Output:** 5
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — only two variables for first and second largest.
```js
function secondLargest(arr) {
  let first = -Infinity, second = -Infinity;
  for (let num of arr) {
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num !== first) {
      second = num;
    }
  }
  return second;
}
```

16. **Find Missing Number in Array (1 to n)**
- **Explanation:** Finds the missing number in an array containing numbers from 1 to n.
- **Input:** [1, 2, 4, 5], n = 5
- **Output:** 3
- **Time Complexity:** O(n) — sum and reduce are O(n).
- **Space Complexity:** O(1) — uses a few variables.
```js
function missingNumber(arr, n) {
  let total = (n * (n + 1)) / 2;
  let sum = arr.reduce((a, b) => a + b, 0);
  return total - sum;
}
```

17. **Find Duplicate Number in Array**
- **Explanation:** Finds a duplicate number in an array. Used to test set/hash logic.
- **Input:** [1, 3, 4, 2, 2]
- **Output:** 2
- **Time Complexity:** O(n) — each element is checked once.
- **Space Complexity:** O(n) — set stores up to n elements.
```js
function findDuplicate(arr) {
  let set = new Set();
  for (let num of arr) {
    if (set.has(num)) return num;
    set.add(num);
  }
  return -1;
}
```

18. **Count Vowels in String**
- **Explanation:** Counts the number of vowels in a string. String traversal and regex.
- **Input:** "hello world"
- **Output:** 3
- **Time Complexity:** O(n) — regex match scans the string once.
- **Space Complexity:** O(1) — only a counter is used.
```js
function countVowels(str) {
  return (str.match(/[aeiou]/gi) || []).length;
}
```

19. **Count Words in String**
- **Explanation:** Counts the number of words in a string. String splitting and trimming.
- **Input:** "hello world! How are you?"
- **Output:** 5
- **Time Complexity:** O(n) — split and trim are O(n).
- **Space Complexity:** O(n) — split creates an array of words.
```js
function countWords(str) {
  return str.trim().split(/\s+/).length;
}
```

20. **Check Anagram**
- **Explanation:** Checks if two strings are anagrams (contain the same characters in any order).
- **Input:** "listen", "silent"
- **Output:** true
- **Time Complexity:** O(n log n) — sorting both strings.
- **Space Complexity:** O(n) — new arrays for sorted strings.
```js
function isAnagram(str1, str2) {
  return str1.split('').sort().join('') === str2.split('').sort().join('');
}
```

---

21. **Find All Substrings of String**
- **Explanation:** Generates all possible substrings of a string. Useful for substring and pattern problems.
- **Input:** "abc"
- **Output:** ["a", "ab", "abc", "b", "bc", "c"]
- **Time Complexity:** O(n^2) — two nested loops for all substrings.
- **Space Complexity:** O(n^2) — stores all substrings.
```js
function allSubstrings(str) {
  let res = [];
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j <= str.length; j++) {
      res.push(str.slice(i, j));
    }
  }
  return res;
}
```

22. **Check Pangram**
- **Explanation:** Checks if a string contains every letter of the English alphabet at least once.
- **Input:** "The quick brown fox jumps over the lazy dog"
- **Output:** true
- **Time Complexity:** O(n) — scans the string once.
- **Space Complexity:** O(1) — set size is at most 26.
```js
function isPangram(str) {
  return new Set(str.toLowerCase().replace(/[^a-z]/g, '')).size === 26;
}
```

23. **Find Power of a Number**
- **Explanation:** Calculates the result of raising a base to an exponent.
- **Input:** 2, 5
- **Output:** 32
- **Time Complexity:** O(1) — uses Math.pow (constant time for JS numbers).
- **Space Complexity:** O(1) — uses a few variables.
```js
function power(base, exp) {
  return Math.pow(base, exp);
}
```

24. **Find Sum of Digits**
- **Explanation:** Sums the digits of a number. Used in digit manipulation problems.
- **Input:** 1234
- **Output:** 10
- **Time Complexity:** O(d) — d is the number of digits.
- **Space Complexity:** O(1) — uses a few variables.
```js
function sumOfDigits(n) {
  return n.toString().split('').reduce((a, b) => a + +b, 0);
}
```

25. **Check Leap Year**
- **Explanation:** Checks if a year is a leap year. Common date logic question.
- **Input:** 2024
- **Output:** true
- **Time Complexity:** O(1) — simple arithmetic checks.
- **Space Complexity:** O(1) — uses a few variables.
```js
function isLeapYear(year) {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
```

26. **Find Largest Word in String**
- **Explanation:** Finds the largest (longest) word in a string.
- **Input:** "I love programming"
- **Output:** "programming"
- **Time Complexity:** O(n) — splits and scans all words.
- **Space Complexity:** O(n) — stores array of words.
```js
function largestWord(str) {
  return str.split(' ').reduce((a, b) => a.length >= b.length ? a : b);
}
```

27. **Capitalize First Letter of Each Word**
- **Explanation:** Capitalizes the first letter of every word in a string.
- **Input:** "hello world"
- **Output:** "Hello World"
- **Time Complexity:** O(n) — regex scans the string once.
- **Space Complexity:** O(n) — creates a new string.
```js
function capitalizeWords(str) {
  return str.replace(/\b\w/g, c => c.toUpperCase());
}
```

28. **Check if Array is Sorted**
- **Explanation:** Checks if an array is sorted in ascending order.
- **Input:** [1, 2, 3, 4]
- **Output:** true
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — uses a few variables.
```js
function isSorted(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) return false;
  }
  return true;
}
```

29. **Sort Array (Bubble Sort)**
- **Explanation:** Sorts an array using the bubble sort algorithm. Classic sorting interview question.
- **Input:** [4, 2, 1, 3]
- **Output:** [1, 2, 3, 4]
- **Time Complexity:** O(n^2) — two nested loops.
- **Space Complexity:** O(1) — sorts in place.
```js
function bubbleSort(arr) {
  let n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}
```

30. **Sort Array (Selection Sort)**
- **Explanation:** Sorts an array using the selection sort algorithm.
- **Input:** [4, 2, 1, 3]
- **Output:** [1, 2, 3, 4]
- **Time Complexity:** O(n^2) — two nested loops.
- **Space Complexity:** O(1) — sorts in place.
```js
function selectionSort(arr) {
  let n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let min = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[min]) min = j;
    }
    [arr[i], arr[min]] = [arr[min], arr[i]];
  }
  return arr;
}
```

31. **Sort Array (Insertion Sort)**
- **Explanation:** Sorts an array using the insertion sort algorithm.
- **Input:** [4, 2, 1, 3]
- **Output:** [1, 2, 3, 4]
- **Time Complexity:** O(n^2) — worst case for nearly reversed arrays.
- **Space Complexity:** O(1) — sorts in place.
```js
function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let key = arr[i], j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  return arr;
}
```

32. **Binary Search in Array**
- **Explanation:** Performs binary search on a sorted array. Classic search algorithm.
- **Input:** [1, 2, 3, 4, 5], 3
- **Output:** 2
- **Time Complexity:** O(log n) — halves the search space each time.
- **Space Complexity:** O(1) — uses a few variables.
```js
function binarySearch(arr, x) {
  let l = 0, r = arr.length - 1;
  while (l <= r) {
    let m = Math.floor((l + r) / 2);
    if (arr[m] === x) return m;
    if (arr[m] < x) l = m + 1;
    else r = m - 1;
  }
  return -1;
}
```

33. **Linear Search in Array**
- **Explanation:** Performs linear search on an array. Basic search algorithm.
- **Input:** [1, 2, 3, 4, 5], 3
- **Output:** 2
- **Time Complexity:** O(n) — checks each element once.
- **Space Complexity:** O(1) — uses a few variables.
```js
function linearSearch(arr, x) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === x) return i;
  }
  return -1;
}
```

34. **Find Intersection of Two Arrays**
- **Explanation:** Finds common elements in two arrays. Set and filter usage.
- **Input:** [1, 2, 3], [2, 3, 4]
- **Output:** [2, 3]
- **Time Complexity:** O(n*m) — for each element in arr1, checks arr2 (can be O(n+m) with sets).
- **Space Complexity:** O(n) — result array and possible set.
```js
function intersection(arr1, arr2) {
  return arr1.filter(x => arr2.includes(x));
}
```

35. **Find Union of Two Arrays**
- **Explanation:** Finds the union of two arrays (all unique elements). Set usage.
- **Input:** [1, 2, 3], [3, 4, 5]
- **Output:** [1, 2, 3, 4, 5]
- **Time Complexity:** O(n + m) — combines and deduplicates both arrays.
- **Space Complexity:** O(n + m) — stores all unique elements.
```js
function union(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}
```

36. **Find All Pairs with Given Sum**
- **Explanation:** Finds all pairs of numbers in an array that sum to a given value. Hash map usage.
- **Input:** [1, 2, 3, 4, 5], sum = 5
- **Output:** [[1, 4], [2, 3]]
- **Time Complexity:** O(n) — each element is checked once.
- **Space Complexity:** O(n) — set stores seen elements.
```js
function pairsWithSum(arr, sum) {
  let res = [];
  let set = new Set();
  for (let num of arr) {
    if (set.has(sum - num)) res.push([num, sum - num]);
    set.add(num);
  }
  return res;
}
```

37. **Move Zeros to End of Array**
- **Explanation:** Moves all zeros in an array to the end while maintaining order. Filter and length usage.
- **Input:** [0, 1, 0, 3, 12]
- **Output:** [1, 3, 12, 0, 0]
- **Time Complexity:** O(n) — filters and fills zeros in one pass each.
- **Space Complexity:** O(n) — creates a new array.
```js
function moveZeros(arr) {
  let nonZero = arr.filter(x => x !== 0);
  let zeros = arr.length - nonZero.length;
  return [...nonZero, ...Array(zeros).fill(0)];
}
```

38. **Left Rotate Array by 1**
- **Explanation:** Rotates an array to the left by one position. Shift and push usage.
- **Input:** [1, 2, 3, 4, 5]
- **Output:** [2, 3, 4, 5, 1]
- **Time Complexity:** O(n) — shift is O(n), push is O(1).
- **Space Complexity:** O(1) — modifies array in place.
```js
function leftRotate(arr) {
  arr.push(arr.shift());
  return arr;
}
```

39. **Right Rotate Array by 1**
- **Explanation:** Rotates an array to the right by one position. Pop and unshift usage.
- **Input:** [1, 2, 3, 4, 5]
- **Output:** [5, 1, 2, 3, 4]
- **Time Complexity:** O(n) — unshift is O(n), pop is O(1).
- **Space Complexity:** O(1) — modifies array in place.
```js
function rightRotate(arr) {
  arr.unshift(arr.pop());
  return arr;
}
```

40. **Find Frequency of Elements in Array**
- **Explanation:** Returns the frequency of each element in an array. Reduce and object usage.
- **Input:** [1, 2, 2, 3, 3, 3]
- **Output:** {1: 1, 2: 2, 3: 3}
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(n) — stores frequency object.
```js
function frequency(arr) {
  let freq = {};
  for (let num of arr) {
    freq[num] = (freq[num] || 0) + 1;
  }
  return freq;
}
```

---

41. **Find First Non-Repeating Character**
- **Explanation:** Finds the first character in a string that does not repeat. Useful for hash map and string problems.
- **Input:** "aabbcdeff"
- **Output:** "c"
- **Time Complexity:** O(n) — two passes: one for frequency, one for first unique.
- **Space Complexity:** O(1) — at most 26 (or 256) chars in hash map.
```js
function firstNonRepeating(str) {
  let freq = {};
  for (let c of str) freq[c] = (freq[c] || 0) + 1;
  for (let c of str) if (freq[c] === 1) return c;
  return null;
}
```

42. **Find Longest Palindromic Substring**
- **Explanation:** Finds the longest substring in a string that is a palindrome. Classic string and DP problem.
- **Input:** "babad"
- **Output:** "bab" or "aba"
- **Time Complexity:** O(n^3) — checks all substrings and reverses each.
- **Space Complexity:** O(n) — for substring and reverse.
```js
function longestPalindrome(s) {
  let res = '';
  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j <= s.length; j++) {
      let sub = s.slice(i, j);
      if (sub === sub.split('').reverse().join('') && sub.length > res.length) res = sub;
    }
  }
  return res;
}
```

43. **Check Balanced Parentheses**
- **Explanation:** Checks if all parentheses in a string are balanced. Stack-based problem.
- **Input:** "(())()"
- **Output:** true
- **Time Complexity:** O(n) — single pass through string.
- **Space Complexity:** O(n) — stack can grow to n/2 in worst case.
```js
function isBalanced(str) {
  let stack = [];
  for (let c of str) {
    if (c === '(') stack.push(c);
    else if (c === ')') {
      if (!stack.length) return false;
      stack.pop();
    }
  }
  return stack.length === 0;
}
```

44. **Find Length of Longest Word**
- **Explanation:** Returns the length of the longest word in a string.
- **Input:** "I love programming"
- **Output:** 11
- **Time Complexity:** O(n) — splits and scans all words.
- **Space Complexity:** O(n) — stores array of words.
```js
function longestWordLength(str) {
  return Math.max(...str.split(' ').map(w => w.length));
}
```

45. **Check if Two Strings are Rotations**
- **Explanation:** Checks if one string is a rotation of another.
- **Input:** "abcd", "cdab"
- **Output:** true
- **Time Complexity:** O(n) — concatenation and includes are O(n).
- **Space Complexity:** O(n) — concatenated string is 2n.
```js
function areRotations(str1, str2) {
  return str1.length === str2.length && (str1 + str1).includes(str2);
}
```

46. **Find Common Elements in Three Arrays**
- **Explanation:** Finds elements common to three arrays. Set and intersection logic.
- **Input:** [1,2,3], [2,3,4], [3,4,5]
- **Output:** [3]
- **Time Complexity:** O(n*m*k) — checks each element in all arrays (can be improved with sets).
- **Space Complexity:** O(n) — result array and possible sets.
```js
function commonElements(arr1, arr2, arr3) {
  return arr1.filter(x => arr2.includes(x) && arr3.includes(x));
}
```

47. **Find Majority Element in Array**
- **Explanation:** Finds the element that appears more than n/2 times in the array.
- **Input:** [3,2,3]
- **Output:** 3
- **Time Complexity:** O(n) — single pass (Boyer-Moore algorithm).
- **Space Complexity:** O(1) — uses a few variables.
```js
function majorityElement(nums) {
  let count = 0, candidate = null;
  for (let num of nums) {
    if (count === 0) candidate = num;
    count += (num === candidate) ? 1 : -1;
  }
  return candidate;
}
```

48. **Find Missing Number**
- **Explanation:** Finds the missing number in an array containing numbers from 0 to n.
- **Input:** [3,0,1]
- **Output:** 2
- **Time Complexity:** O(n) — single pass to sum.
- **Space Complexity:** O(1) — uses a few variables.
```js
function missingNumber(nums) {
  let n = nums.length;
  let sum = n * (n + 1) / 2;
  return sum - nums.reduce((a, b) => a + b, 0);
}
```

49. **Find First Unique Character in String**
- **Explanation:** Returns the index of the first non-repeating character.
- **Input:** "leetcode"
- **Output:** 0
- **Time Complexity:** O(n) — two passes through string.
- **Space Complexity:** O(1) — at most 26 letters in map.
```js
function firstUniqChar(s) {
  let map = {};
  for (let c of s) map[c] = (map[c] || 0) + 1;
  for (let i = 0; i < s.length; i++) if (map[s[i]] === 1) return i;
  return -1;
}
```

50. **Find Intersection of Two Arrays**
- **Explanation:** Returns the intersection of two arrays.
- **Input:** [1,2,2,1], [2,2]
- **Output:** [2]
- **Time Complexity:** O(n + m) — n and m are array lengths.
- **Space Complexity:** O(min(n, m)) — set for smaller array.
```js
function intersection(nums1, nums2) {
  let set1 = new Set(nums1), set2 = new Set(nums2);
  return [...set1].filter(x => set2.has(x));
}
```

51. **Find Longest Consecutive Sequence**
- **Explanation:** Finds the length of the longest consecutive elements sequence.
- **Input:** [100,4,200,1,3,2]
- **Output:** 4
- **Time Complexity:** O(n) — each number checked at most twice.
- **Space Complexity:** O(n) — set for all numbers.
```js
function longestConsecutive(nums) {
  let set = new Set(nums), max = 0;
  for (let num of set) {
    if (!set.has(num - 1)) {
      let len = 1;
      while (set.has(num + len)) len++;
      max = Math.max(max, len);
    }
  }
  return max;
}
```

52. **Find Single Number**
- **Explanation:** Every element appears twice except for one. Find that one.
- **Input:** [4,1,2,1,2]
- **Output:** 4
- **Time Complexity:** O(n) — single pass.
- **Space Complexity:** O(1) — uses XOR.
```js
function singleNumber(nums) {
  return nums.reduce((a, b) => a ^ b, 0);
}
```

53. **Find Duplicate Number**
- **Explanation:** Finds the duplicate number in an array of n+1 integers where each integer is between 1 and n.
- **Input:** [1,3,4,2,2]
- **Output:** 2
- **Time Complexity:** O(n) — Floyd's Tortoise and Hare.
- **Space Complexity:** O(1) — constant space.
```js
function findDuplicate(nums) {
  let slow = nums[0], fast = nums[0];
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
}
```

54. **Find Minimum in Rotated Sorted Array**
- **Explanation:** Finds the minimum element in a rotated sorted array.
- **Input:** [3,4,5,1,2]
- **Output:** 1
- **Time Complexity:** O(log n) — binary search.
- **Space Complexity:** O(1) — uses a few variables.
```js
function findMin(nums) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (nums[m] > nums[r]) l = m + 1;
    else r = m;
  }
  return nums[l];
}
```

55. **Find Peak Element**
- **Explanation:** Finds a peak element (greater than neighbors).
- **Input:** [1,2,3,1]
- **Output:** 2
- **Time Complexity:** O(log n) — binary search.
- **Space Complexity:** O(1) — uses a few variables.
```js
function findPeakElement(nums) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (nums[m] < nums[m + 1]) l = m + 1;
    else r = m;
  }
  return l;
}
```

56. **Find Kth Largest Element in Array**
- **Explanation:** Finds the kth largest element using a min-heap or quickselect.
- **Input:** [3,2,1,5,6,4], k = 2
- **Output:** 5
- **Time Complexity:** O(n) average (quickselect), O(n log k) (heap).
- **Space Complexity:** O(1) (quickselect), O(k) (heap).
```js
function findKthLargest(nums, k) {
  nums.sort((a, b) => b - a);
  return nums[k - 1];
}
```

57. **Find All Anagrams in String**
- **Explanation:** Finds all starting indices of anagrams of a pattern in a string.
- **Input:** s = "cbaebabacd", p = "abc"
- **Output:** [0,6]
- **Time Complexity:** O(n) — sliding window.
- **Space Complexity:** O(1) — at most 26 letters in map.
```js
function findAnagrams(s, p) {
  let res = [], map = {}, count = p.length, l = 0;
  for (let c of p) map[c] = (map[c] || 0) + 1;
  for (let r = 0; r < s.length; r++) {
    if (map[s[r]]-- > 0) count--;
    if (r - l + 1 > p.length && ++map[s[l++]] > 0) count++;
    if (count === 0) res.push(l);
  }
  return res;
}
```

58. **Find Longest Palindromic Substring**
- **Explanation:** Finds the longest palindromic substring in a string.
- **Input:** "babad"
- **Output:** "bab" or "aba"
- **Time Complexity:** O(n^2) — expand around center.
- **Space Complexity:** O(1) — only a few variables.
```js
function longestPalindrome(s) {
  let start = 0, end = 0;
  for (let i = 0; i < s.length; i++) {
    let len1 = expand(s, i, i), len2 = expand(s, i, i + 1);
    let len = Math.max(len1, len2);
    if (len > end - start) {
      start = i - Math.floor((len - 1) / 2);
      end = i + Math.floor(len / 2);
    }
  }
  return s.slice(start, end + 1);
}
function expand(s, l, r) {
  while (l >= 0 && r < s.length && s[l] === s[r]) {
    l--;
    r++;
  }
  return r - l - 1;
}
```

59. **Find Shortest Path in Binary Matrix**
- **Explanation:** Finds the shortest path from top-left to bottom-right in a binary matrix.
- **Input:** [[0,1],[1,0]]
- **Output:** 2
- **Time Complexity:** O(n^2) — BFS on n x n grid.
- **Space Complexity:** O(n^2) — queue and visited set.
```js
function shortestPathBinaryMatrix(grid) {
  let n = grid.length;
  if (grid[0][0] || grid[n-1][n-1]) return -1;
  let q = [[0,0,1]], dirs = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]];
  let seen = Array.from({length:n},()=>Array(n).fill(false));
  seen[0][0]=true;
  while(q.length){
    let [x,y,d]=q.shift();
    if(x===n-1&&y===n-1)return d;
    for(let [dx,dy] of dirs){
      let nx=x+dx,ny=y+dy;
      if(nx>=0&&ny>=0&&nx<n&&ny<n&&!seen[nx][ny]&&!grid[nx][ny]){
        seen[nx][ny]=true;
        q.push([nx,ny,d+1]);
      }
    }
  }
  return -1;
}
```

60. **Find Number of Islands**
- **Explanation:** Counts the number of islands in a 2D grid.
- **Input:** [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
- **Output:** 3
- **Time Complexity:** O(m*n) — visit every cell.
- **Space Complexity:** O(m*n) — recursion stack or queue.
```js
function numIslands(grid) {
  let count = 0;
  function dfs(i, j) {
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] === '0') return;
    grid[i][j] = '0';
    dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1);
  }
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === '1') {
        count++;
        dfs(i, j);
      }
    }
  }
  return count;
}
```

61. **Find Minimum Path Sum**
- **Explanation:** Finds the minimum path sum from top-left to bottom-right in a grid.
- **Input:** [[1,3,1],[1,5,1],[4,2,1]]
- **Output:** 7
- **Time Complexity:** O(m*n) — DP for each cell.
- **Space Complexity:** O(m*n) — DP table.
```js
function minPathSum(grid) {
  let m = grid.length, n = grid[0].length;
  let dp = Array(m).fill().map(()=>Array(n).fill(0));
  dp[0][0]=grid[0][0];
  for(let i=1;i<m;i++)dp[i][0]=dp[i-1][0]+grid[i][0];
  for(let j=1;j<n;j++)dp[0][j]=dp[0][j-1]+grid[0][j];
  for(let i=1;i<m;i++){
    for(let j=1;j<n;j++){
      dp[i][j]=grid[i][j]+Math.min(dp[i-1][j],dp[i][j-1]);
    }
  }
  return dp[m-1][n-1];
}
```

62. **Find Unique Paths**
- **Explanation:** Finds the number of unique paths from top-left to bottom-right in a grid.
- **Input:** m = 3, n = 7
- **Output:** 28
- **Time Complexity:** O(m*n) — DP for each cell.
- **Space Complexity:** O(m*n) — DP table.
```js
function uniquePaths(m, n) {
  let dp = Array(m).fill().map(()=>Array(n).fill(1));
  for(let i=1;i<m;i++){
    for(let j=1;j<n;j++){
      dp[i][j]=dp[i-1][j]+dp[i][j-1];
    }
  }
  return dp[m-1][n-1];
}
```

63. **Find Climbing Stairs Ways**
- **Explanation:** Finds the number of ways to climb n stairs (1 or 2 steps at a time).
- **Input:** 3
- **Output:** 3
- **Time Complexity:** O(n) — single pass.
- **Space Complexity:** O(1) — only two variables needed.
```js
function climbStairs(n) {
  let a = 1, b = 1;
  for (let i = 2; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}
```

64. **Find Coin Change Ways**
- **Explanation:** Finds the minimum number of coins to make up a given amount.
- **Input:** coins = [1,2,5], amount = 11
- **Output:** 3
- **Time Complexity:** O(amount * n) — n is number of coins.
- **Space Complexity:** O(amount) — DP array.
```js
function coinChange(coins, amount) {
  let dp = Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}
```

65. **Find Subsets of Array**
- **Explanation:** Returns all possible subsets (the power set) of an array.
- **Input:** [1,2,3]
- **Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
- **Time Complexity:** O(2^n * n) — 2^n subsets, each up to n elements.
- **Space Complexity:** O(2^n * n) — stores all subsets.
```js
function subsets(nums) {
  let res = [[]];
  for (let num of nums) {
    res = res.concat(res.map(arr => arr.concat(num)));
  }
  return res;
}
```

66. **Find Permutations of Array**
- **Explanation:** Returns all possible permutations of an array.
- **Input:** [1,2,3]
- **Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
- **Time Complexity:** O(n * n!) — n! permutations, each of length n.
- **Space Complexity:** O(n * n!) — stores all permutations.
```js
function permute(nums) {
  let res = [];
  function backtrack(path, used) {
    if (path.length === nums.length) res.push([...path]);
    else {
      for (let i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.push(nums[i]);
        backtrack(path, used);
        path.pop();
        used[i] = false;
      }
    }
  }
  backtrack([], Array(nums.length).fill(false));
  return res;
}
```

---

67. **Find Leaders in Array**
- **Explanation:** Finds all leaders in an array (elements greater than all elements to their right).
- **Input:** [16,17,4,3,5,2]
- **Output:** [17,5,2]
- **Time Complexity:** O(n) — single pass from right to left.
- **Space Complexity:** O(n) — stores leaders.
```js
function leaders(arr) {
  let max = -Infinity, res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] > max) {
      max = arr[i];
      res.push(max);
    }
  }
  return res.reverse();
}
```

68. **Find Equilibrium Index of Array**
- **Explanation:** Finds the index where the sum of elements to the left equals the sum to the right.
- **Input:** [-7,1,5,2,-4,3,0]
- **Output:** 3
- **Time Complexity:** O(n) — two passes: total sum and scan.
- **Space Complexity:** O(1) — uses a few variables.
```js
function equilibriumIndex(arr) {
  let total = arr.reduce((a, b) => a + b, 0), left = 0;
  for (let i = 0; i < arr.length; i++) {
    total -= arr[i];
    if (left === total) return i;
    left += arr[i];
  }
  return -1;
}
```

69. **Find Maximum Product Subarray**
- **Explanation:** Finds the maximum product of a contiguous subarray.
- **Input:** [2,3,-2,4]
- **Output:** 6
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — uses a few variables.
```js
function maxProductSubarray(arr) {
  let max = arr[0], min = arr[0], res = arr[0];
  for (let i = 1; i < arr.length; i++) {
    let temp = max;
    max = Math.max(arr[i], max * arr[i], min * arr[i]);
    min = Math.min(arr[i], temp * arr[i], min * arr[i]);
    res = Math.max(res, max);
  }
  return res;
}
```

70. **Find Minimum Window Substring**
- **Explanation:** Finds the minimum window in a string which contains all characters of another string.
- **Input:** s = "ADOBECODEBANC", t = "ABC"
- **Output:** "BANC"
- **Time Complexity:** O(n + m) — n is s length, m is t length.
- **Space Complexity:** O(m) — hash map for t's chars.
```js
function minWindow(s, t) {
  let map = {}, count = t.length, l = 0, res = '';
  for (let c of t) map[c] = (map[c] || 0) + 1;
  for (let r = 0; r < s.length; r++) {
    if (map[s[r]]-- > 0) count--;
    while (count === 0) {
      if (!res || r - l + 1 < res.length) res = s.slice(l, r + 1);
      if (++map[s[l++]] > 0) count++;
    }
  }
  return res;
}
```

71. **Find All Palindromic Substrings**
- **Explanation:** Finds all substrings of a string that are palindromes.
- **Input:** "ababa"
- **Output:** ["a", "aba", "ababa", "b", "bab", "a", "b", "a"]
- **Time Complexity:** O(n^3) — checks all substrings and reverses each.
- **Space Complexity:** O(n^2) — stores all palindromic substrings.
```js
function allPalindromicSubstrings(str) {
  let res = [];
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j <= str.length; j++) {
      let sub = str.slice(i, j);
      if (sub === sub.split('').reverse().join('')) res.push(sub);
    }
  }
  return res;
}
```

72. **Find Longest Common Prefix**
- **Explanation:** Finds the longest common prefix among an array of strings.
- **Input:** ["flower","flow","flight"]
- **Output:** "fl"
- **Time Complexity:** O(n*m) — n strings, m is average length.
- **Space Complexity:** O(1) — only a few variables.
```js
function longestCommonPrefix(arr) {
  if (!arr.length) return '';
  let prefix = arr[0];
  for (let str of arr) {
    while (!str.startsWith(prefix)) {
      prefix = prefix.slice(0, -1);
      if (!prefix) return '';
    }
  }
  return prefix;
}
```

73. **Find Longest Common Subsequence**
- **Explanation:** Finds the length of the longest subsequence common to two strings. Classic DP problem.
- **Input:** "abcde", "ace"
- **Output:** 3
- **Time Complexity:** O(n*m) — n and m are string lengths.
- **Space Complexity:** O(n*m) — DP table.
```js
function lcs(a, b) {
  let dp = Array(a.length + 1).fill().map(() => Array(b.length + 1).fill(0));
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
      else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
  return dp[a.length][b.length];
}
```

74. **Find Longest Increasing Subsequence**
- **Explanation:** Finds the length of the longest increasing subsequence in an array.
- **Input:** [10,9,2,5,3,7,101,18]
- **Output:** 4
- **Time Complexity:** O(n^2) — nested loops for DP.
- **Space Complexity:** O(n) — DP array.
```js
function lis(arr) {
  let dp = Array(arr.length).fill(1);
  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] > arr[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
  return Math.max(...dp);
}
```

75. **Find Edit Distance (Levenshtein Distance)**
- **Explanation:** Finds the minimum number of operations to convert one string to another.
- **Input:** "kitten", "sitting"
- **Output:** 3
- **Time Complexity:** O(n*m) — n and m are string lengths.
- **Space Complexity:** O(n*m) — DP table.
```js
function editDistance(a, b) {
  let dp = Array(a.length + 1).fill().map(() => Array(b.length + 1).fill(0));
  for (let i = 0; i <= a.length; i++) dp[i][0] = i;
  for (let j = 0; j <= b.length; j++) dp[0][j] = j;
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }
  return dp[a.length][b.length];
}
```

76. **Find Minimum Jumps to Reach End**
- **Explanation:** Finds the minimum number of jumps to reach the end of an array.
- **Input:** [2,3,1,1,4]
- **Output:** 2
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — uses a few variables.
```js
function minJumps(arr) {
  let jumps = 0, end = 0, far = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    far = Math.max(far, i + arr[i]);
    if (i === end) {
      jumps++;
      end = far;
    }
  }
  return jumps;
}
```

77. **Find Leaders in Array**
- **Explanation:** Finds all leaders in an array (elements greater than all elements to their right).
- **Input:** [16,17,4,3,5,2]
- **Output:** [17,5,2]
- **Time Complexity:** O(n) — single pass from right to left.
- **Space Complexity:** O(n) — stores leaders.
```js
function leaders(arr) {
  let max = -Infinity, res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] > max) {
      max = arr[i];
      res.push(max);
    }
  }
  return res.reverse();
}
```

78. **Find Equilibrium Index of Array**
- **Explanation:** Finds the index where the sum of elements to the left equals the sum to the right.
- **Input:** [-7,1,5,2,-4,3,0]
- **Output:** 3
- **Time Complexity:** O(n) — two passes: total sum and scan.
- **Space Complexity:** O(1) — uses a few variables.
```js
function equilibriumIndex(arr) {
  let total = arr.reduce((a, b) => a + b, 0), left = 0;
  for (let i = 0; i < arr.length; i++) {
    total -= arr[i];
    if (left === total) return i;
    left += arr[i];
  }
  return -1;
}
```

79. **Find Maximum Product Subarray**
- **Explanation:** Finds the maximum product of a contiguous subarray.
- **Input:** [2,3,-2,4]
- **Output:** 6
- **Time Complexity:** O(n) — single pass through array.
- **Space Complexity:** O(1) — uses a few variables.
```js
function maxProductSubarray(arr) {
  let max = arr[0], min = arr[0], res = arr[0];
  for (let i = 1; i < arr.length; i++) {
    let temp = max;
    max = Math.max(arr[i], max * arr[i], min * arr[i]);
    min = Math.min(arr[i], temp * arr[i], min * arr[i]);
    res = Math.max(res, max);
  }
  return res;
}
```

80. **Find Minimum Window Substring**
- **Explanation:** Finds the minimum window in a string which contains all characters of another string.
- **Input:** s = "ADOBECODEBANC", t = "ABC"
- **Output:** "BANC"
- **Time Complexity:** O(n + m) — n is s length, m is t length.
- **Space Complexity:** O(m) — hash map for t's chars.
```js
function minWindow(s, t) {
  let map = {}, count = t.length, l = 0, res = '';
  for (let c of t) map[c] = (map[c] || 0) + 1;
  for (let r = 0; r < s.length; r++) {
    if (map[s[r]]-- > 0) count--;
    while (count === 0) {
      if (!res || r - l + 1 < res.length) res = s.slice(l, r + 1);
      if (++map[s[l++]] > 0) count++;
    }
  }
  return res;
}
```

81. **Find the Majority Element**
- **Explanation:** Finds the element that appears more than n/2 times in the array.
- **Input:** [3,2,3]
- **Output:** 3
- **Time Complexity:** O(n) — single pass (Boyer-Moore algorithm).
- **Space Complexity:** O(1) — uses a few variables.
```js
function majorityElement(nums) {
  let count = 0, candidate = null;
  for (let num of nums) {
    if (count === 0) candidate = num;
    count += (num === candidate) ? 1 : -1;
  }
  return candidate;
}
```

82. **Find the Missing Number**
- **Explanation:** Finds the missing number in an array containing numbers from 0 to n.
- **Input:** [3,0,1]
- **Output:** 2
- **Time Complexity:** O(n) — single pass to sum.
- **Space Complexity:** O(1) — uses a few variables.
```js
function missingNumber(nums) {
  let n = nums.length;
  let sum = n * (n + 1) / 2;
  return sum - nums.reduce((a, b) => a + b, 0);
}
```

83. **Find the First Unique Character in a String**
- **Explanation:** Returns the index of the first non-repeating character.
- **Input:** "leetcode"
- **Output:** 0
- **Time Complexity:** O(n) — two passes through string.
- **Space Complexity:** O(1) — at most 26 letters in map.
```js
function firstUniqChar(s) {
  let map = {};
  for (let c of s) map[c] = (map[c] || 0) + 1;
  for (let i = 0; i < s.length; i++) if (map[s[i]] === 1) return i;
  return -1;
}
```

84. **Find the Intersection of Two Arrays**
- **Explanation:** Returns the intersection of two arrays.
- **Input:** [1,2,2,1], [2,2]
- **Output:** [2]
- **Time Complexity:** O(n + m) — n and m are array lengths.
- **Space Complexity:** O(min(n, m)) — set for smaller array.
```js
function intersection(nums1, nums2) {
  let set1 = new Set(nums1), set2 = new Set(nums2);
  return [...set1].filter(x => set2.has(x));
}
```

85. **Find the Longest Consecutive Sequence**
- **Explanation:** Finds the length of the longest consecutive elements sequence.
- **Input:** [100,4,200,1,3,2]
- **Output:** 4
- **Time Complexity:** O(n) — each number checked at most twice.
- **Space Complexity:** O(n) — set for all numbers.
```js
function longestConsecutive(nums) {
  let set = new Set(nums), max = 0;
  for (let num of set) {
    if (!set.has(num - 1)) {
      let len = 1;
      while (set.has(num + len)) len++;
      max = Math.max(max, len);
    }
  }
  return max;
}
```

86. **Find the Single Number**
- **Explanation:** Every element appears twice except for one. Find that one.
- **Input:** [4,1,2,1,2]
- **Output:** 4
- **Time Complexity:** O(n) — single pass.
- **Space Complexity:** O(1) — uses XOR.
```js
function singleNumber(nums) {
  return nums.reduce((a, b) => a ^ b, 0);
}
```

87. **Find the Duplicate Number**
- **Explanation:** Finds the duplicate number in an array of n+1 integers where each integer is between 1 and n.
- **Input:** [1,3,4,2,2]
- **Output:** 2
- **Time Complexity:** O(n) — Floyd's Tortoise and Hare.
- **Space Complexity:** O(1) — constant space.
```js
function findDuplicate(nums) {
  let slow = nums[0], fast = nums[0];
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
}
```

88. **Find the Minimum in Rotated Sorted Array**
- **Explanation:** Finds the minimum element in a rotated sorted array.
- **Input:** [3,4,5,1,2]
- **Output:** 1
- **Time Complexity:** O(log n) — binary search.
- **Space Complexity:** O(1) — uses a few variables.
```js
function findMin(nums) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (nums[m] > nums[r]) l = m + 1;
    else r = m;
  }
  return nums[l];
}
```

89. **Find Peak Element**
- **Explanation:** Finds a peak element (greater than neighbors).
- **Input:** [1,2,3,1]
- **Output:** 2
- **Time Complexity:** O(log n) — binary search.
- **Space Complexity:** O(1) — uses a few variables.
```js
function findPeakElement(nums) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (nums[m] < nums[m + 1]) l = m + 1;
    else r = m;
  }
  return l;
}
```

90. **Find the Kth Largest Element in an Array**
- **Explanation:** Finds the kth largest element using a min-heap or quickselect.
- **Input:** [3,2,1,5,6,4], k = 2
- **Output:** 5
- **Time Complexity:** O(n) average (quickselect), O(n log k) (heap).
- **Space Complexity:** O(1) (quickselect), O(k) (heap).
```js
function findKthLargest(nums, k) {
  nums.sort((a, b) => b - a);
  return nums[k - 1];
}
```

91. **Find All Anagrams in a String**
- **Explanation:** Finds all start indices of p's anagrams in s.
- **Input:** s = "cbaebabacd", p = "abc"
- **Output:** [0,6]
- **Time Complexity:** O(n) — sliding window.
- **Space Complexity:** O(1) — at most 26 letters in map.
```js
function findAnagrams(s, p) {
  let res = [], map = {}, count = p.length, l = 0;
  for (let c of p) map[c] = (map[c] || 0) + 1;
  for (let r = 0; r < s.length; r++) {
    if (map[s[r]]-- > 0) count--;
    if (r - l + 1 > p.length && ++map[s[l++]] > 0) count++;
    if (count === 0) res.push(l);
  }
  return res;
}
```

92. **Find the Longest Palindromic Substring**
- **Explanation:** Finds the longest palindromic substring in a string.
- **Input:** "babad"
- **Output:** "bab" or "aba"
- **Time Complexity:** O(n^2) — expand around center.
- **Space Complexity:** O(1) — only a few variables.
```js
function longestPalindrome(s) {
  let start = 0, end = 0;
  for (let i = 0; i < s.length; i++) {
    let len1 = expand(s, i, i), len2 = expand(s, i, i + 1);
    let len = Math.max(len1, len2);
    if (len > end - start) {
      start = i - Math.floor((len - 1) / 2);
      end = i + Math.floor(len / 2);
    }
  }
  return s.slice(start, end + 1);
}
function expand(s, l, r) {
  while (l >= 0 && r < s.length && s[l] === s[r]) {
    l--;
    r++;
  }
  return r - l - 1;
}
```

93. **Find the Shortest Path in a Binary Matrix**
- **Explanation:** Finds the shortest path from top-left to bottom-right in a binary matrix.
- **Input:** [[0,1],[1,0]]
- **Output:** 2
- **Time Complexity:** O(n^2) — BFS on n x n grid.
- **Space Complexity:** O(n^2) — queue and visited set.
```js
function shortestPathBinaryMatrix(grid) {
  let n = grid.length;
  if (grid[0][0] || grid[n-1][n-1]) return -1;
  let q = [[0,0,1]], dirs = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]];
  let seen = Array.from({length:n},()=>Array(n).fill(false));
  seen[0][0]=true;
  while(q.length){
    let [x,y,d]=q.shift();
    if(x===n-1&&y===n-1)return d;
    for(let [dx,dy] of dirs){
      let nx=x+dx,ny=y+dy;
      if(nx>=0&&ny>=0&&nx<n&&ny<n&&!seen[nx][ny]&&!grid[nx][ny]){
        seen[nx][ny]=true;
        q.push([nx,ny,d+1]);
      }
    }
  }
  return -1;
}
```

94. **Find the Number of Islands**
- **Explanation:** Counts the number of islands in a 2D grid.
- **Input:** [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
- **Output:** 3
- **Time Complexity:** O(m*n) — visit every cell.
- **Space Complexity:** O(m*n) — recursion stack or queue.
```js
function numIslands(grid) {
  let count = 0;
  function dfs(i, j) {
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] === '0') return;
    grid[i][j] = '0';
    dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1);
  }
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === '1') {
        count++;
        dfs(i, j);
      }
    }
  }
  return count;
}
```

95. **Find the Minimum Path Sum**
- **Explanation:** Finds the minimum path sum from top-left to bottom-right in a grid.
- **Input:** [[1,3,1],[1,5,1],[4,2,1]]
- **Output:** 7
- **Time Complexity:** O(m*n) — DP for each cell.
- **Space Complexity:** O(m*n) — DP table.
```js
function minPathSum(grid) {
  let m = grid.length, n = grid[0].length;
  let dp = Array(m).fill().map(()=>Array(n).fill(0));
  dp[0][0]=grid[0][0];
  for(let i=1;i<m;i++)dp[i][0]=dp[i-1][0]+grid[i][0];
  for(let j=1;j<n;j++)dp[0][j]=dp[0][j-1]+grid[0][j];
  for(let i=1;i<m;i++){
    for(let j=1;j<n;j++){
      dp[i][j]=grid[i][j]+Math.min(dp[i-1][j],dp[i][j-1]);
    }
  }
  return dp[m-1][n-1];
}
```

96. **Find the Unique Paths**
- **Explanation:** Finds the number of unique paths from top-left to bottom-right in a grid.
- **Input:** m = 3, n = 7
- **Output:** 28
- **Time Complexity:** O(m*n) — DP for each cell.
- **Space Complexity:** O(m*n) — DP table.
```js
function uniquePaths(m, n) {
  let dp = Array(m).fill().map(()=>Array(n).fill(1));
  for(let i=1;i<m;i++){
    for(let j=1;j<n;j++){
      dp[i][j]=dp[i-1][j]+dp[i][j-1];
    }
  }
  return dp[m-1][n-1];
}
```

97. **Find the Climbing Stairs Ways**
- **Explanation:** Finds the number of ways to climb n stairs (1 or 2 steps at a time).
- **Input:** 3
- **Output:** 3
- **Time Complexity:** O(n) — single pass.
- **Space Complexity:** O(1) — only two variables needed.
```js
function climbStairs(n) {
  let a = 1, b = 1;
  for (let i = 2; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}
```

98. **Find the Coin Change Ways**
- **Explanation:** Finds the minimum number of coins to make up a given amount.
- **Input:** coins = [1,2,5], amount = 11
- **Output:** 3
- **Time Complexity:** O(amount * n) — n is number of coins.
- **Space Complexity:** O(amount) — DP array.
```js
function coinChange(coins, amount) {
  let dp = Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}
```

99. **Find the Subsets of an Array**
- **Explanation:** Returns all possible subsets (the power set) of an array.
- **Input:** [1,2,3]
- **Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
- **Time Complexity:** O(2^n * n) — 2^n subsets, each up to n elements.
- **Space Complexity:** O(2^n * n) — stores all subsets.
```js
function subsets(nums) {
  let res = [[]];
  for (let num of nums) {
    res = res.concat(res.map(arr => arr.concat(num)));
  }
  return res;
}
```

100. **Find the Permutations of an Array**
- **Explanation:** Returns all possible permutations of an array.
- **Input:** [1,2,3]
- **Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
- **Time Complexity:** O(n * n!) — n! permutations, each of length n.
- **Space Complexity:** O(n * n!) — stores all permutations.
```js
function permute(nums) {
  let res = [];
  function backtrack(path, used) {
    if (path.length === nums.length) res.push([...path]);
    else {
      for (let i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.push(nums[i]);
        backtrack(path, used);
        path.pop();
        used[i] = false;
      }
    }
  }
  backtrack([], Array(nums.length).fill(false));
  return res;
}
```