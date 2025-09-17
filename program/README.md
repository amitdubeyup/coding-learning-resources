# 100 Most Common Coding Interview Programs (JavaScript)

Below are 100 easy to medium level programs frequently asked in coding interviews at companies like WIPRO, TCS, INFOSYS, ACCENTURE, CAPGEMINI, HCL TECH, TECH MAHINDRA, IBM, DELOITTE, COGNIZANT, etc. Each program includes a JavaScript solution.

---

1. **Reverse a String**
- **Explanation:** Reverses the characters in a string. Common for string manipulation and basic logic.
- **Input:** "hello"
- **Output:** "olleh"
```js
function reverseString(str) {
  return str.split('').reverse().join('');
}
```

2. **Check for Palindrome**
- **Explanation:** Checks if a string reads the same forwards and backwards. Palindrome checks are common in interviews.
- **Input:** "madam"
- **Output:** true
```js
function isPalindrome(str) {
  return str === str.split('').reverse().join('');
}
```

3. **Find Factorial**
- **Explanation:** Calculates the factorial of a number. Used to test recursion and loops.
- **Input:** 5
- **Output:** 120
```js
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}
```

4. **Find Fibonacci Number**
- **Explanation:** Returns the nth Fibonacci number. Used to test recursion and dynamic programming basics.
- **Input:** 6
- **Output:** 8
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
```js
function largest(arr) {
  return Math.max(...arr);
}
```

6. **Find Smallest Element in Array**
- **Explanation:** Finds the smallest number in an array.
- **Input:** [1, 5, 2, 9, 3]
- **Output:** 1
```js
function smallest(arr) {
  return Math.min(...arr);
}
```

7. **Sum of Array Elements**
- **Explanation:** Sums all elements in an array. Used to test array methods and loops.
- **Input:** [1, 2, 3, 4]
- **Output:** 10
```js
function sumArray(arr) {
  return arr.reduce((a, b) => a + b, 0);
}
```

8. **Remove Duplicates from Array**
- **Explanation:** Removes duplicate values from an array. Set usage is a common topic.
- **Input:** [1, 2, 2, 3, 4, 4]
- **Output:** [1, 2, 3, 4]
```js
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
```

9. **Check if Number is Prime**
- **Explanation:** Checks if a number is prime. Prime logic is a classic interview question.
- **Input:** 7
- **Output:** true
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
```js
function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}
```

12. **Find LCM of Two Numbers**
- **Explanation:** Finds the least common multiple (LCM) of two numbers. Often paired with GCD.
- **Input:** 4, 6
- **Output:** 12
```js
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}
```

13. **Check Armstrong Number**
- **Explanation:** Checks if a number is an Armstrong number (sum of its own digits each raised to the power of the number of digits equals the number itself).
- **Input:** 153
- **Output:** true
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
```js
function countVowels(str) {
  return (str.match(/[aeiou]/gi) || []).length;
}
```

19. **Count Words in String**
- **Explanation:** Counts the number of words in a string. String splitting and trimming.
- **Input:** "hello world! How are you?"
- **Output:** 5
```js
function countWords(str) {
  return str.trim().split(/\s+/).length;
}
```

20. **Check Anagram**
- **Explanation:** Checks if two strings are anagrams (contain the same characters in any order).
- **Input:** "listen", "silent"
- **Output:** true
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
```js
function isPangram(str) {
  return new Set(str.toLowerCase().replace(/[^a-z]/g, '')).size === 26;
}
```

23. **Find Power of a Number**
- **Explanation:** Calculates the result of raising a base to an exponent.
- **Input:** 2, 5
- **Output:** 32
```js
function power(base, exp) {
  return Math.pow(base, exp);
}
```

24. **Find Sum of Digits**
- **Explanation:** Sums the digits of a number. Used in digit manipulation problems.
- **Input:** 1234
- **Output:** 10
```js
function sumOfDigits(n) {
  return n.toString().split('').reduce((a, b) => a + +b, 0);
}
```

25. **Check Leap Year**
- **Explanation:** Checks if a year is a leap year. Common date logic question.
- **Input:** 2024
- **Output:** true
```js
function isLeapYear(year) {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
```

26. **Find Largest Word in String**
- **Explanation:** Finds the largest (longest) word in a string.
- **Input:** "I love programming"
- **Output:** "programming"
```js
function largestWord(str) {
  return str.split(' ').reduce((a, b) => a.length >= b.length ? a : b);
}
```

27. **Capitalize First Letter of Each Word**
- **Explanation:** Capitalizes the first letter of every word in a string.
- **Input:** "hello world"
- **Output:** "Hello World"
```js
function capitalizeWords(str) {
  return str.replace(/\b\w/g, c => c.toUpperCase());
}
```

28. **Check if Array is Sorted**
- **Explanation:** Checks if an array is sorted in ascending order.
- **Input:** [1, 2, 3, 4]
- **Output:** true
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
```js
function intersection(arr1, arr2) {
  return arr1.filter(x => arr2.includes(x));
}
```

35. **Find Union of Two Arrays**
- **Explanation:** Finds the union of two arrays (all unique elements). Set usage.
- **Input:** [1, 2, 3], [3, 4, 5]
- **Output:** [1, 2, 3, 4, 5]
```js
function union(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}
```

36. **Find All Pairs with Given Sum**
- **Explanation:** Finds all pairs of numbers in an array that sum to a given value. Hash map usage.
- **Input:** [1, 2, 3, 4, 5], sum = 5
- **Output:** [[1, 4], [2, 3]]
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
```js
function longestWordLength(str) {
  return Math.max(...str.split(' ').map(w => w.length));
}
```

45. **Check if Two Strings are Rotations**
- **Explanation:** Checks if one string is a rotation of another.
- **Input:** "abcd", "cdab"
- **Output:** true
```js
function areRotations(str1, str2) {
  return str1.length === str2.length && (str1 + str1).includes(str2);
}
```

46. **Find Common Elements in Three Arrays**
- **Explanation:** Finds elements common to three arrays. Set and intersection logic.
- **Input:** [1,2,3], [2,3,4], [3,4,5]
- **Output:** [3]
```js
function commonElements(arr1, arr2, arr3) {
  return arr1.filter(x => arr2.includes(x) && arr3.includes(x));
}
```

47. **Find Majority Element in Array**
- **Explanation:** Finds the element that appears more than n/2 times in an array. Boyer-Moore Voting Algorithm.
- **Input:** [3,3,4,2,3,3,5]
- **Output:** 3
```js
function majorityElement(arr) {
  let count = 0, candidate = null;
  for (let num of arr) {
    if (count === 0) candidate = num;
    count += (num === candidate) ? 1 : -1;
  }
  count = arr.filter(x => x === candidate).length;
  return count > arr.length / 2 ? candidate : null;
}
```

48. **Find Subarray with Given Sum**
- **Explanation:** Finds the start and end indices of a subarray that sums to a given value. Hash map and prefix sum logic.
- **Input:** [1,2,3,7,5], sum = 12
- **Output:** [2, 4]
```js
function subarraySum(arr, sum) {
  let curr = 0, map = {0: -1};
  for (let i = 0; i < arr.length; i++) {
    curr += arr[i];
    if ((curr - sum) in map) return [map[curr - sum] + 1, i];
    map[curr] = i;
  }
  return null;
}
```

49. **Find All Permutations of String**
- **Explanation:** Generates all permutations of a string. Recursion and backtracking.
- **Input:** "abc"
- **Output:** ["abc", "acb", "bac", "bca", "cab", "cba"]
```js
function permutations(str) {
  if (str.length <= 1) return [str];
  let res = [];
  for (let i = 0; i < str.length; i++) {
    let rest = str.slice(0, i) + str.slice(i + 1);
    for (let perm of permutations(rest)) {
      res.push(str[i] + perm);
    }
  }
  return res;
}
```

50. **Find All Subsets of Array**
- **Explanation:** Generates all possible subsets (the power set) of an array. Recursion and bitmasking.
- **Input:** [1,2,3]
- **Output:** [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```js
function subsets(arr) {
  let res = [[]];
  for (let num of arr) {
    res = res.concat(res.map(sub => sub.concat(num)));
  }
  return res;
}
```

---

51. **Find Kth Largest Element**
- **Explanation:** Finds the kth largest element in an array. Sorting and selection logic.
- **Input:** [3,2,1,5,6,4], k = 2
- **Output:** 5
```js
function kthLargest(arr, k) {
  return arr.sort((a, b) => b - a)[k - 1];
}
```

52. **Find Kth Smallest Element**
- **Explanation:** Finds the kth smallest element in an array.
- **Input:** [3,2,1,5,6,4], k = 2
- **Output:** 2
```js
function kthSmallest(arr, k) {
  return arr.sort((a, b) => a - b)[k - 1];
}
```

53. **Find Peak Element in Array**
- **Explanation:** Finds a peak element (greater than neighbors) in an array.
- **Input:** [1,2,3,1]
- **Output:** 3
```js
function findPeak(arr) {
  for (let i = 1; i < arr.length - 1; i++) {
    if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) return arr[i];
  }
  return null;
}
```

54. **Find Missing and Repeating Number**
- **Explanation:** Finds the missing and repeating numbers in an array of 1 to n.
- **Input:** [4, 3, 6, 2, 1, 1], n = 6
- **Output:** {missing: 5, repeating: 1}
```js
function findMissingRepeating(arr, n) {
  let set = new Set();
  let repeating, total = (n * (n + 1)) / 2, sum = 0;
  for (let num of arr) {
    if (set.has(num)) repeating = num;
    set.add(num);
    sum += num;
  }
  let missing = total - (sum - repeating);
  return {missing, repeating};
}
```

55. **Find First and Last Occurrence of Element**
- **Explanation:** Finds the first and last index of an element in an array.
- **Input:** [5,7,7,8,8,10], x = 8
- **Output:** [3, 4]
```js
function firstLastOccurrence(arr, x) {
  return [arr.indexOf(x), arr.lastIndexOf(x)];
}
```

56. **Find All Duplicates in Array**
- **Explanation:** Returns all duplicate elements in an array.
- **Input:** [4,3,2,7,8,2,3,1]
- **Output:** [2, 3]
```js
function allDuplicates(arr) {
  let seen = new Set(), res = new Set();
  for (let num of arr) {
    if (seen.has(num)) res.add(num);
    seen.add(num);
  }
  return Array.from(res);
}
```

57. **Find Longest Consecutive Sequence**
- **Explanation:** Finds the length of the longest consecutive sequence in an array.
- **Input:** [100, 4, 200, 1, 3, 2]
- **Output:** 4
```js
function longestConsecutive(arr) {
  let set = new Set(arr), max = 0;
  for (let num of set) {
    if (!set.has(num - 1)) {
      let len = 1, curr = num;
      while (set.has(curr + 1)) {
        curr++;
        len++;
      }
      max = Math.max(max, len);
    }
  }
  return max;
}
```

58. **Find Minimum in Rotated Sorted Array**
- **Explanation:** Finds the minimum element in a rotated sorted array.
- **Input:** [3,4,5,1,2]
- **Output:** 1
```js
function findMinRotated(arr) {
  let l = 0, r = arr.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (arr[m] > arr[r]) l = m + 1;
    else r = m;
  }
  return arr[l];
}
```

59. **Find Maximum Subarray Sum (Kadane's Algorithm)**
- **Explanation:** Finds the maximum sum of a contiguous subarray. Classic DP problem.
- **Input:** [-2,1,-3,4,-1,2,1,-5,4]
- **Output:** 6
```js
function maxSubArray(arr) {
  let max = arr[0], curr = arr[0];
  for (let i = 1; i < arr.length; i++) {
    curr = Math.max(arr[i], curr + arr[i]);
    max = Math.max(max, curr);
  }
  return max;
}
```

60. **Find Subsets with Given Sum**
- **Explanation:** Finds all subsets of an array that sum to a given value.
- **Input:** [1,2,3], sum = 3
- **Output:** [[1,2], [3]]
```js
function subsetSum(arr, sum) {
  let res = [];
  function dfs(i, curr, total) {
    if (i === arr.length) {
      if (total === sum) res.push([...curr]);
      return;
    }
    dfs(i + 1, curr, total);
    curr.push(arr[i]);
    dfs(i + 1, curr, total + arr[i]);
    curr.pop();
  }
  dfs(0, [], 0);
  return res;
}
```

---

61. **Find All Palindromic Substrings**
- **Explanation:** Finds all substrings of a string that are palindromes.
- **Input:** "ababa"
- **Output:** ["a", "aba", "ababa", "b", "bab", "a", "b", "a"]
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

62. **Find Longest Common Prefix**
- **Explanation:** Finds the longest common prefix among an array of strings.
- **Input:** ["flower","flow","flight"]
- **Output:** "fl"
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

63. **Find Longest Common Subsequence**
- **Explanation:** Finds the length of the longest subsequence common to two strings. Classic DP problem.
- **Input:** "abcde", "ace"
- **Output:** 3
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

64. **Find Longest Increasing Subsequence**
- **Explanation:** Finds the length of the longest increasing subsequence in an array.
- **Input:** [10,9,2,5,3,7,101,18]
- **Output:** 4
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

65. **Find Edit Distance (Levenshtein Distance)**
- **Explanation:** Finds the minimum number of operations to convert one string to another.
- **Input:** "kitten", "sitting"
- **Output:** 3
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

66. **Find Minimum Jumps to Reach End**
- **Explanation:** Finds the minimum number of jumps to reach the end of an array.
- **Input:** [2,3,1,1,4]
- **Output:** 2
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

67. **Find Leaders in Array**
- **Explanation:** Finds all leaders in an array (elements greater than all elements to their right).
- **Input:** [16,17,4,3,5,2]
- **Output:** [17,5,2]
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

---

71. **Find All Perfect Numbers in Range**
- **Explanation:** Finds all perfect numbers in a given range.
- **Input:** 1, 30
- **Output:** [6, 28]
```js
function perfectNumbers(start, end) {
  let res = [];
  for (let i = start; i <= end; i++) {
    if (isPerfect(i)) res.push(i);
  }
  return res;
}
```

72. **Find All Prime Factors of Number**
- **Explanation:** Returns all prime factors of a number.
- **Input:** 28
- **Output:** [2, 2, 7]
```js
function primeFactors(n) {
  let res = [];
  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i === 0) {
      res.push(i);
      n /= i;
    }
  }
  if (n > 1) res.push(n);
  return res;
}
```

73. **Find Power Set of String**
- **Explanation:** Returns all possible subsets (power set) of a string.
- **Input:** "abc"
- **Output:** ["", "a", "b", "c", "ab", "ac", "bc", "abc"]
```js
function powerSet(str) {
  let res = [''];
  for (let c of str) {
    res = res.concat(res.map(s => s + c));
  }
  return res;
}
```

74. **Find All Substrings with Distinct Characters**
- **Explanation:** Finds all substrings of a string with all unique characters.
- **Input:** "abc"
- **Output:** ["a", "ab", "abc", "b", "bc", "c"]
```js
function substringsWithDistinctChars(str) {
  let res = [];
  for (let i = 0; i < str.length; i++) {
    let set = new Set();
    for (let j = i; j < str.length; j++) {
      if (set.has(str[j])) break;
      set.add(str[j]);
      res.push(str.slice(i, j + 1));
    }
  }
  return res;
}
```

75. **Find All Subarrays with Distinct Elements**
- **Explanation:** Finds all subarrays of an array with all unique elements.
- **Input:** [1,2,3]
- **Output:** [[1],[1,2],[1,2,3],[2],[2,3],[3]]
```js
function subarraysWithDistinct(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let set = new Set();
    for (let j = i; j < arr.length; j++) {
      if (set.has(arr[j])) break;
      set.add(arr[j]);
      res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

76. **Find All Subarrays with Even Sum**
- **Explanation:** Finds all subarrays whose sum is even.
- **Input:** [1,2,3]
- **Output:** [[1, 3], [2], [2, 3]]
```js
function subarraysWithEvenSum(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (sum % 2 === 0) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

77. **Find All Subarrays with Odd Sum**
- **Explanation:** Finds all subarrays whose sum is odd.
- **Input:** [1,2,3]
- **Output:** [[1],[1,2],[2,3],[3]]
```js
function subarraysWithOddSum(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (sum % 2 !== 0) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

78. **Find All Subarrays with Product Less Than K**
- **Explanation:** Finds all subarrays whose product is less than k.
- **Input:** [10, 5, 2, 6], k = 100
- **Output:** [[10], [5], [10,5], [2], [5,2], [6], [2,6], [5,2,6]]
```js
function subarraysWithProductLessThanK(arr, k) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let prod = 1;
    for (let j = i; j < arr.length; j++) {
      prod *= arr[j];
      if (prod < k) res.push(arr.slice(i, j + 1));
      else break;
    }
  }
  return res;
}
```

79. **Find All Subarrays with Maximum Sum**
- **Explanation:** Finds all subarrays whose sum equals the maximum subarray sum.
- **Input:** [1, -2, 3, 4, -1, 2, 1, -5, 4]
- **Output:** [[3,4,-1,2,1]]
```js
function subarraysWithMaxSum(arr) {
  let max = maxSubArray(arr), res = [];
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (sum === max) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

80. **Find All Subarrays with Minimum Sum**
- **Explanation:** Finds all subarrays whose sum equals the minimum subarray sum.
- **Input:** [1, -2, 3, 4, -1, 2, 1, -5, 4]
- **Output:** [[-5]]
```js
function subarraysWithMinSum(arr) {
  let min = Math.min(...arr), res = [];
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (sum === min) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

---

81. **Find All Anagrams in String**
- **Explanation:** Finds all starting indices of anagrams of a pattern in a string.
- **Input:** s = "cbaebabacd", p = "abc"
- **Output:** [0, 6]
```js
function findAnagrams(s, p) {
  let res = [], map = {}, left = 0, right = 0, count = p.length;
  for (let c of p) map[c] = (map[c] || 0) + 1;
  while (right < s.length) {
    if (map[s[right++]]-- > 0) count--;
    if (count === 0) res.push(left);
    if (right - left === p.length && map[s[left]]++ >= 0) count++;
    left++;
  }
  return res;
}
```

82. **Check if String is Rotation of Another (using Substring)**
- **Explanation:** Checks if one string is a rotation of another using substring method.
- **Input:** "waterbottle", "erbottlewat"
- **Output:** true
```js
function isRotation(str1, str2) {
  return str1.length === str2.length && (str1 + str1).includes(str2);
}
```

83. **Find Minimum Number of Platforms Required for Railway Station**
- **Explanation:** Finds the minimum number of platforms required to accommodate all trains at a railway station.
- **Input:** arr = [10, 15, 25, 30], dep = [20, 25, 35, 40]
- **Output:** 2
```js
function minPlatforms(arr, dep) {
  let platforms = 0, maxPlatforms = 0;
  let i = 0, j = 0;
  while (i < arr.length && j < dep.length) {
    if (arr[i] < dep[j]) {
      platforms++;
      i++;
      maxPlatforms = Math.max(maxPlatforms, platforms);
    } else {
      platforms--;
      j++;
    }
  }
  return maxPlatforms;
}
```

84. **Find Median of Two Sorted Arrays**
- **Explanation:** Finds the median of two sorted arrays. Classic binary search and merge problem.
- **Input:** nums1 = [1, 3], nums2 = [2]
- **Output:** 2
```js
function findMedianSortedArrays(nums1, nums2) {
  let merged = [], i = 0, j = 0;
  while (i < nums1.length || j < nums2.length) {
    if (i === nums1.length) merged.push(nums2[j++]);
    else if (j === nums2.length) merged.push(nums1[i++]);
    else if (nums1[i] < nums2[j]) merged.push(nums1[i++]);
    else merged.push(nums2[j++]);
  }
  let mid = Math.floor(merged.length / 2);
  return merged.length % 2 === 0 ? (merged[mid - 1] + merged[mid]) / 2 : merged[mid];
}
```

85. **Find First Missing Positive Integer**
- **Explanation:** Finds the smallest positive integer missing from an array.
- **Input:** [3, 4, -1, 1]
- **Output:** 2
```js
function firstMissingPositive(nums) {
  let set = new Set(nums);
  for (let i = 1; i <= nums.length + 1; i++) {
    if (!set.has(i)) return i;
  }
}
```

86. **Find All Unique Triplets in Array that Sum to Zero**
- **Explanation:** Finds all unique triplets in an array that sum up to zero. Classic three-sum problem.
- **Input:** [-1, 0, 1, 2, -1, -4]
- **Output:** [[-1, -1, 2], [-1, 0, 1]]
```js
function threeSum(nums) {
  let res = [];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      let sum = nums[i] + nums[l] + nums[r];
      if (sum === 0) {
        res.push([nums[i], nums[l], nums[r]]);
        while (l < r && nums[l] === nums[l + 1]) l++;
        while (l < r && nums[r] === nums[r - 1]) r--;
        l++;
        r--;
      } else if (sum < 0) l++;
      else r--;
    }
  }
  return res;
}
```

87. **Sort Colors (Dutch National Flag Problem)**
- **Explanation:** Sorts an array of 0s, 1s, and 2s (representing colors) in a single pass.
- **Input:** [2, 0, 2, 1, 1, 0]
- **Output:** [0, 0, 1, 1, 2, 2]
```js
function sortColors(nums) {
  let low = 0, mid = 0, high = nums.length - 1;
  while (mid <= high) {
    if (nums[mid] === 0) [nums[low++], nums[mid++]] = [nums[mid], nums[low]];
    else if (nums[mid] === 2) [nums[mid], nums[high--]] = [nums[high], nums[mid]];
    else mid++;
  }
}
```

88. **Search in Rotated Sorted Array**
- **Explanation:** Searches for a target value in a rotated sorted array.
- **Input:** nums = [4,5,6,7,0,1,2], target = 0
- **Output:** 4
```js
function search(nums, target) {
  let l = 0, r = nums.length - 1;
  while (l <= r) {
    let m = Math.floor((l + r) / 2);
    if (nums[m] === target) return m;
    if (nums[l] <= nums[m]) {
      if (target >= nums[l] && target < nums[m]) r = m - 1;
      else l = m + 1;
    } else {
      if (target > nums[m] && target <= nums[r]) l = m + 1;
      else r = m - 1;
    }
  }
  return -1;
}
```

89. **Find Minimum in Rotated Sorted Array II (with Duplicates)**
- **Explanation:** Finds the minimum element in a rotated sorted array that may contain duplicates.
- **Input:** [2,2,2,0,1,2]
- **Output:** 0
```js
function findMin(arr) {
  let l = 0, r = arr.length - 1;
  while (l < r) {
    if (arr[l] < arr[r]) return arr[l];
    let m = Math.floor((l + r) / 2);
    if (arr[m] > arr[r]) l = m + 1;
    else if (arr[m] < arr[r]) r = m;
    else r--;
  }
  return arr[l];
}
```

90. **Maximum Product of Three Numbers**
- **Explanation:** Finds the maximum product of three numbers in an array.
- **Input:** [1, 2, 3, 4]
- **Output:** 24
```js
function maximumProduct(nums) {
  nums.sort((a, b) => a - b);
  let n = nums.length;
  return Math.max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1]);
}
```

---

91. **Find All Subarrays with Given XOR**
- **Explanation:** Finds all subarrays whose XOR equals a given value.
- **Input:** [4, 2, 2, 6, 4], k = 6
- **Output:** [[2,2,6],[6]]
```js
function subarraysWithXOR(arr, k) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let xor = 0;
    for (let j = i; j < arr.length; j++) {
      xor ^= arr[j];
      if (xor === k) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

92. **Find All Subarrays with Given Product**
- **Explanation:** Finds all subarrays whose product equals a given value.
- **Input:** [2, 4, 1, 6], prod = 8
- **Output:** [[2,4]]
```js
function subarraysWithProduct(arr, prod) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let p = 1;
    for (let j = i; j < arr.length; j++) {
      p *= arr[j];
      if (p === prod) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

93. **Find All Subarrays with Maximum Product**
- **Explanation:** Finds all subarrays whose product equals the maximum product subarray.
- **Input:** [2,3,-2,4]
- **Output:** [[2,3]]
```js
function subarraysWithMaxProduct(arr) {
  let max = maxProductSubarray(arr), res = [];
  for (let i = 0; i < arr.length; i++) {
    let prod = 1;
    for (let j = i; j < arr.length; j++) {
      prod *= arr[j];
      if (prod === max) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

94. **Find All Subarrays with Minimum Product**
- **Explanation:** Finds all subarrays whose product equals the minimum product subarray.
- **Input:** [2,3,-2,4]
- **Output:** [[-2]]
```js
function subarraysWithMinProduct(arr) {
  let min = Math.min(...arr), res = [];
  for (let i = 0; i < arr.length; i++) {
    let prod = 1;
    for (let j = i; j < arr.length; j++) {
      prod *= arr[j];
      if (prod === min) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

95. **Find All Subarrays with Maximum Length**
- **Explanation:** Finds all subarrays with the maximum possible length (the whole array).
- **Input:** [1,2,3]
- **Output:** [[1,2,3]]
```js
function subarraysWithMaxLength(arr) {
  let max = arr.length, res = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i; j < arr.length; j++) {
      if (j - i + 1 === max) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

96. **Find All Subarrays with Minimum Length**
- **Explanation:** Finds all subarrays with the minimum possible length (single elements).
- **Input:** [1,2,3]
- **Output:** [[1],[2],[3]]
```js
function subarraysWithMinLength(arr) {
  let min = 1, res = [];
  for (let i = 0; i < arr.length; i++) {
    res.push([arr[i]]);
  }
  return res;
}
```

97. **Find All Subarrays with Even Length**
- **Explanation:** Finds all subarrays with even length.
- **Input:** [1,2,3,4]
- **Output:** [[1,2],[2,3],[3,4],[1,2,3,4]]
```js
function subarraysWithEvenLength(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j += 2) {
      res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

98. **Find All Subarrays with Odd Length**
- **Explanation:** Finds all subarrays with odd length.
- **Input:** [1,2,3]
- **Output:** [[1],[2],[3],[1,2,3]]
```js
function subarraysWithOddLength(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i; j < arr.length; j += 2) {
      res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

99. **Find All Subarrays with Prime Sum**
- **Explanation:** Finds all subarrays whose sum is a prime number.
- **Input:** [1,2,3]
- **Output:** [[2],[3],[1,2],[2,3]]
```js
function subarraysWithPrimeSum(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (isPrime(sum)) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

100. **Find All Subarrays with Palindromic Concatenation**
- **Explanation:** Finds all subarrays whose concatenation forms a palindrome.
- **Input:** ["a","b","a"]
- **Output:** [["a"],["b"],["a"],["a","b","a"]]
```js
function subarraysWithPalindromicConcat(arr) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let str = '';
    for (let j = i; j < arr.length; j++) {
      str += arr[j];
      if (str === str.split('').reverse().join('')) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

---

Feel free to use and practice these programs for your coding interviews!