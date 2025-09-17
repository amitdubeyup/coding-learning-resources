# 100 Most Common Coding Interview Programs (JavaScript)

Below are 100 easy to medium level programs frequently asked in coding interviews at companies like WIPRO, TCS, INFOSYS, ACCENTURE, CAPGEMINI, HCL TECH, TECH MAHINDRA, IBM, DELOITTE, COGNIZANT, etc. Each program includes a JavaScript solution.

---

1. **Reverse a String**
    ```js
    function reverseString(str) {
      return str.split('').reverse().join('');
    }
    ```

2. **Check for Palindrome**
    ```js
    function isPalindrome(str) {
      return str === str.split('').reverse().join('');
    }
    ```

3. **Find Factorial**
    ```js
    function factorial(n) {
      return n <= 1 ? 1 : n * factorial(n - 1);
    }
    ```

4. **Find Fibonacci Number**
    ```js
    function fibonacci(n) {
      if (n <= 1) return n;
      return fibonacci(n - 1) + fibonacci(n - 2);
    }
    ```

5. **Find Largest Element in Array**
    ```js
    function largest(arr) {
      return Math.max(...arr);
    }
    ```

6. **Find Smallest Element in Array**
    ```js
    function smallest(arr) {
      return Math.min(...arr);
    }
    ```

7. **Sum of Array Elements**
    ```js
    function sumArray(arr) {
      return arr.reduce((a, b) => a + b, 0);
    }
    ```

8. **Remove Duplicates from Array**
    ```js
    function removeDuplicates(arr) {
      return [...new Set(arr)];
    }
    ```

9. **Check if Number is Prime**
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
```js
function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}
```

12. **Find LCM of Two Numbers**
```js
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}
```

13. **Check Armstrong Number**
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
```js
function missingNumber(arr, n) {
  let total = (n * (n + 1)) / 2;
  let sum = arr.reduce((a, b) => a + b, 0);
  return total - sum;
}
```

17. **Find Duplicate Number in Array**
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
```js
function countVowels(str) {
  return (str.match(/[aeiou]/gi) || []).length;
}
```

19. **Count Words in String**
```js
function countWords(str) {
  return str.trim().split(/\s+/).length;
}
```

20. **Check Anagram**
```js
function isAnagram(str1, str2) {
  return str1.split('').sort().join('') === str2.split('').sort().join('');
}
```

21. **Find All Substrings of String**
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
```js
function isPangram(str) {
  return new Set(str.toLowerCase().replace(/[^a-z]/g, '')).size === 26;
}
```

23. **Find Power of a Number**
```js
function power(base, exp) {
  return Math.pow(base, exp);
}
```

24. **Find Sum of Digits**
```js
function sumOfDigits(n) {
  return n.toString().split('').reduce((a, b) => a + +b, 0);
}
```

25. **Check Leap Year**
```js
function isLeapYear(year) {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
```

26. **Find Largest Word in String**
```js
function largestWord(str) {
  return str.split(' ').reduce((a, b) => a.length >= b.length ? a : b);
}
```

27. **Capitalize First Letter of Each Word**
```js
function capitalizeWords(str) {
  return str.replace(/\b\w/g, c => c.toUpperCase());
}
```

28. **Check if Array is Sorted**
```js
function isSorted(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) return false;
  }
  return true;
}
```

29. **Sort Array (Bubble Sort)**
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
```js
function linearSearch(arr, x) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === x) return i;
  }
  return -1;
}
```

34. **Find Intersection of Two Arrays**
```js
function intersection(arr1, arr2) {
  return arr1.filter(x => arr2.includes(x));
}
```

35. **Find Union of Two Arrays**
```js
function union(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}
```

36. **Find All Pairs with Given Sum**
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
```js
function moveZeros(arr) {
  let nonZero = arr.filter(x => x !== 0);
  let zeros = arr.length - nonZero.length;
  return [...nonZero, ...Array(zeros).fill(0)];
}
```

38. **Left Rotate Array by 1**
```js
function leftRotate(arr) {
  arr.push(arr.shift());
  return arr;
}
```

39. **Right Rotate Array by 1**
```js
function rightRotate(arr) {
  arr.unshift(arr.pop());
  return arr;
}
```

40. **Find Frequency of Elements in Array**
```js
function frequency(arr) {
  let freq = {};
  for (let num of arr) {
    freq[num] = (freq[num] || 0) + 1;
  }
  return freq;
}
```

41. **Find First Non-Repeating Character**
```js
function firstNonRepeating(str) {
  let freq = {};
  for (let c of str) freq[c] = (freq[c] || 0) + 1;
  for (let c of str) if (freq[c] === 1) return c;
  return null;
}
```

42. **Find Longest Palindromic Substring**
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
```js
function longestWordLength(str) {
  return Math.max(...str.split(' ').map(w => w.length));
}
```

45. **Check if Two Strings are Rotations**
```js
function areRotations(str1, str2) {
  return str1.length === str2.length && (str1 + str1).includes(str2);
}
```

46. **Find Common Elements in Three Arrays**
```js
function commonElements(arr1, arr2, arr3) {
  return arr1.filter(x => arr2.includes(x) && arr3.includes(x));
}
```

47. **Find Majority Element in Array**
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
```js
function subsets(arr) {
  let res = [[]];
  for (let num of arr) {
    res = res.concat(res.map(sub => sub.concat(num)));
  }
  return res;
}
```

51. **Find Kth Largest Element**
```js
function kthLargest(arr, k) {
  return arr.sort((a, b) => b - a)[k - 1];
}
```

52. **Find Kth Smallest Element**
```js
function kthSmallest(arr, k) {
  return arr.sort((a, b) => a - b)[k - 1];
}
```

53. **Find Peak Element in Array**
```js
function findPeak(arr) {
  for (let i = 1; i < arr.length - 1; i++) {
    if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) return arr[i];
  }
  return null;
}
```

54. **Find Missing and Repeating Number**
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
```js
function firstLastOccurrence(arr, x) {
  return [arr.indexOf(x), arr.lastIndexOf(x)];
}
```

56. **Find All Duplicates in Array**
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

61. **Find All Palindromic Substrings**
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

71. **Find All Anagrams in String**
```js
function findAnagrams(s, p) {
  let res = [], map = {}, count = p.length;
  for (let c of p) map[c] = (map[c] || 0) + 1;
  let l = 0;
  for (let r = 0; r < s.length; r++) {
    if (map[s[r]]-- > 0) count--;
    if (r - l + 1 > p.length && ++map[s[l++]] > 0) count++;
    if (count === 0) res.push(l);
  }
  return res;
}
```

72. **Find All Unique Triplets with Zero Sum**
```js
function threeSum(arr) {
  arr.sort((a, b) => a - b);
  let res = [];
  for (let i = 0; i < arr.length - 2; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) continue;
    let l = i + 1, r = arr.length - 1;
    while (l < r) {
      let sum = arr[i] + arr[l] + arr[r];
      if (sum === 0) {
        res.push([arr[i], arr[l], arr[r]]);
        while (arr[l] === arr[l + 1]) l++;
        while (arr[r] === arr[r - 1]) r--;
        l++; r--;
      } else if (sum < 0) l++;
      else r--;
    }
  }
  return res;
}
```

73. **Find All Unique Quadruplets with Given Sum**
```js
function fourSum(arr, target) {
  arr.sort((a, b) => a - b);
  let res = [];
  for (let i = 0; i < arr.length - 3; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) continue;
    for (let j = i + 1; j < arr.length - 2; j++) {
      if (j > i + 1 && arr[j] === arr[j - 1]) continue;
      let l = j + 1, r = arr.length - 1;
      while (l < r) {
        let sum = arr[i] + arr[j] + arr[l] + arr[r];
        if (sum === target) {
          res.push([arr[i], arr[j], arr[l], arr[r]]);
          while (arr[l] === arr[l + 1]) l++;
          while (arr[r] === arr[r - 1]) r--;
          l++; r--;
        } else if (sum < target) l++;
        else r--;
      }
    }
  }
  return res;
}
```

74. **Find Median of Two Sorted Arrays**
```js
function findMedianSortedArrays(a, b) {
  let arr = [...a, ...b].sort((x, y) => x - y);
  let n = arr.length;
  return n % 2 ? arr[Math.floor(n / 2)] : (arr[n / 2 - 1] + arr[n / 2]) / 2;
}
```

75. **Find Minimum Difference Pair**
```js
function minDiffPair(arr) {
  arr.sort((a, b) => a - b);
  let min = Infinity, pair = [];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] - arr[i - 1] < min) {
      min = arr[i] - arr[i - 1];
      pair = [arr[i - 1], arr[i]];
    }
  }
  return pair;
}
```

76. **Find Maximum Difference Pair**
```js
function maxDiffPair(arr) {
  arr.sort((a, b) => a - b);
  return [arr[0], arr[arr.length - 1]];
}
```

77. **Find All Pairs with Given Product**
```js
function pairsWithProduct(arr, prod) {
  let res = [], set = new Set(arr);
  for (let num of arr) {
    if (prod % num === 0 && set.has(prod / num) && num !== prod / num) {
      res.push([num, prod / num]);
      set.delete(num);
      set.delete(prod / num);
    }
  }
  return res;
}
```

78. **Find All Subarrays with Given Sum**
```js
function allSubarraysWithSum(arr, sum) {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    let curr = 0;
    for (let j = i; j < arr.length; j++) {
      curr += arr[j];
      if (curr === sum) res.push(arr.slice(i, j + 1));
    }
  }
  return res;
}
```

79. **Find All Palindrome Numbers in Range**
```js
function palindromeNumbers(start, end) {
  let res = [];
  for (let i = start; i <= end; i++) {
    if (i.toString() === i.toString().split('').reverse().join('')) res.push(i);
  }
  return res;
}
```

80. **Find All Armstrong Numbers in Range**
```js
function armstrongNumbers(start, end) {
  let res = [];
  for (let i = start; i <= end; i++) {
    if (isArmstrong(i)) res.push(i);
  }
  return res;
}
```

81. **Find All Perfect Numbers in Range**
```js
function perfectNumbers(start, end) {
  let res = [];
  for (let i = start; i <= end; i++) {
    if (isPerfect(i)) res.push(i);
  }
  return res;
}
```

82. **Find All Prime Factors of Number**
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

83. **Find Power Set of String**
```js
function powerSet(str) {
  let res = [''];
  for (let c of str) {
    res = res.concat(res.map(s => s + c));
  }
  return res;
}
```

84. **Find All Substrings with Distinct Characters**
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

85. **Find All Subarrays with Distinct Elements**
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

86. **Find All Subarrays with Even Sum**
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

87. **Find All Subarrays with Odd Sum**
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

88. **Find All Subarrays with Product Less Than K**
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

89. **Find All Subarrays with Maximum Sum**
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

90. **Find All Subarrays with Minimum Sum**
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

91. **Find All Subarrays with Given XOR**
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