📌 Most Common DSA Interview Topics & Questions
🔹 1. Complexity Basics

Time & Space Complexity (✅ you covered)

Big-O, Big-Ω, Big-Θ differences

Best, Worst, Average cases

### Time & Space Complexity
Time complexity measures how the runtime of an algorithm grows with the input size. Space complexity measures the extra space used by the algorithm.

- **Time Complexity**: Often expressed in Big-O notation, it describes the upper bound of the algorithm's growth rate.
- **Space Complexity**: Measures auxiliary space used, excluding input space.

Example: In JavaScript, a simple loop has O(n) time complexity.

```javascript
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
```

### Big-O, Big-Ω, Big-Θ Differences
- **Big-O (O)**: Upper bound, worst-case scenario. "The algorithm takes at most this much time."
- **Big-Ω (Ω)**: Lower bound, best-case scenario. "The algorithm takes at least this much time."
- **Big-Θ (Θ)**: Tight bound, both upper and lower. "The algorithm takes exactly this much time asymptotically."

Example: Linear search is O(n), Ω(1), Θ(n) in worst, best, average cases respectively.

### Best, Worst, Average Cases
- **Best Case**: Minimum time for any input (e.g., finding element at first position in linear search: Ω(1)).
- **Worst Case**: Maximum time for any input (e.g., element at last position: O(n)).
- **Average Case**: Expected time over all inputs, often Θ(n) for linear search assuming uniform distribution.

🔹 2. Arrays & Strings

Find second largest number (✅ you asked)

Kadane’s Algorithm (Maximum Subarray Sum)

Two Sum problem (Hashing approach)

Sliding Window problems (longest substring without repeat, max sum subarray of size k)

Rotate array (by k steps)

Trapping Rainwater problem

Palindrome (✅ you covered)

Anagrams, Substring/ Subsequence problems

### Find Second Largest Number
To find the second largest number in an array, iterate through the array, keeping track of the largest and second largest elements.

```javascript
function secondLargest(arr) {
    if (arr.length < 2) return null;
    let first = -Infinity, second = -Infinity;
    for (let num of arr) {
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num !== first) {
            second = num;
        }
    }
    return second === -Infinity ? null : second;
}
```

### Kadane’s Algorithm (Maximum Subarray Sum)
Kadane's algorithm finds the maximum sum of a contiguous subarray in O(n) time.

```javascript
function maxSubarraySum(arr) {
    let maxSoFar = arr[0];
    let maxEndingHere = arr[0];
    for (let i = 1; i < arr.length; i++) {
        maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
        maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }
    return maxSoFar;
}
```

### Two Sum Problem (Hashing Approach)
Given an array and a target sum, find two indices that add up to the target using a hash map for O(n) time.

```javascript
function twoSum(arr, target) {
    const map = new Map();
    for (let i = 0; i < arr.length; i++) {
        const complement = target - arr[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(arr[i], i);
    }
    return [];
}
```

### Sliding Window Problems
Sliding window technique maintains a window of elements and slides it to find optimal subarrays.

#### Longest Substring Without Repeating Characters
```javascript
function lengthOfLongestSubstring(s) {
    const set = new Set();
    let left = 0, maxLen = 0;
    for (let right = 0; right < s.length; right++) {
        while (set.has(s[right])) {
            set.delete(s[left]);
            left++;
        }
        set.add(s[right]);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

#### Maximum Sum Subarray of Size K
```javascript
function maxSumSubarray(arr, k) {
    let maxSum = 0, windowSum = 0;
    for (let i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    maxSum = windowSum;
    for (let i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

### Rotate Array by K Steps
Rotate an array to the right by k steps.

```javascript
function rotateArray(arr, k) {
    k %= arr.length;
    reverse(arr, 0, arr.length - 1);
    reverse(arr, 0, k - 1);
    reverse(arr, k, arr.length - 1);
    return arr;
}

function reverse(arr, start, end) {
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }
}
```

### Trapping Rainwater Problem
Calculate trapped rainwater using two pointers or dynamic programming.

```javascript
function trap(height) {
    let left = 0, right = height.length - 1;
    let leftMax = 0, rightMax = 0, water = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            right--;
        }
    }
    return water;
}
```

### Palindrome (✅ you covered)
A palindrome reads the same forwards and backwards. Check by comparing characters from both ends.

```javascript
function isPalindrome(s) {
    s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}
```

### Anagrams, Substring/Subsequence Problems
#### Anagrams: Check if two strings are anagrams by sorting or using frequency count.
```javascript
function isAnagram(s, t) {
    if (s.length !== t.length) return false;
    const count = {};
    for (let char of s) {
        count[char] = (count[char] || 0) + 1;
    }
    for (let char of t) {
        if (!count[char]) return false;
        count[char]--;
    }
    return true;
}
```

#### Substring: Contiguous sequence. Subsequence: Not necessarily contiguous.
```javascript
// Check if s is subsequence of t
function isSubsequence(s, t) {
    let i = 0, j = 0;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) i++;
        j++;
    }
    return i === s.length;
}
```

🔹 3. Searching & Sorting

Binary Search + Variations (first/last occurrence, rotated array search, square root, peak element)

Merge Sort & Quick Sort (time & space complexity ✅ covered partially)

Heap Sort

Counting Sort / Radix Sort basics

### Binary Search + Variations
Binary search finds an element in a sorted array in O(log n) time.

#### Standard Binary Search
```javascript
function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

#### First Occurrence
```javascript
function firstOccurrence(arr, target) {
    let left = 0, right = arr.length - 1, result = -1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            result = mid;
            right = mid - 1;
        } else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return result;
}
```

#### Rotated Array Search
```javascript
function searchRotated(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        if (arr[left] <= arr[mid]) {
            if (target >= arr[left] && target < arr[mid]) right = mid - 1;
            else left = mid + 1;
        } else {
            if (target > arr[mid] && target <= arr[right]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}
```

#### Square Root (Integer)
```javascript
function mySqrt(x) {
    if (x < 2) return x;
    let left = 1, right = x, result = 0;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (mid <= x / mid) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}
```

#### Peak Element
```javascript
function findPeakElement(nums) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] < nums[mid + 1]) left = mid + 1;
        else right = mid;
    }
    return left;
}
```

### Merge Sort & Quick Sort
#### Merge Sort: Divide and conquer, stable, O(n log n) time, O(n) space.
```javascript
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    const result = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) result.push(left[i++]);
        else result.push(right[j++]);
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}
```

#### Quick Sort: Divide and conquer, in-place, O(n log n) average, O(n^2) worst.
```javascript
function quickSort(arr, low = 0, high = arr.length - 1) {
    if (low < high) {
        const pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
    return arr;
}

function partition(arr, low, high) {
    const pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}
```

### Heap Sort
Heap sort uses a heap data structure, O(n log n) time, in-place.

```javascript
function heapSort(arr) {
    const n = arr.length;
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    for (let i = n - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
    return arr;
}

function heapify(arr, n, i) {
    let largest = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
}
```

### Counting Sort / Radix Sort Basics
#### Counting Sort: For small range integers, O(n + k) time.
```javascript
function countingSort(arr) {
    const max = Math.max(...arr);
    const count = new Array(max + 1).fill(0);
    for (let num of arr) count[num]++;
    const result = [];
    for (let i = 0; i <= max; i++) {
        while (count[i] > 0) {
            result.push(i);
            count[i]--;
        }
    }
    return result;
}
```

#### Radix Sort: Sorts by digits, O(n * d) time where d is digit count.
```javascript
function radixSort(arr) {
    const max = Math.max(...arr);
    let exp = 1;
    while (Math.floor(max / exp) > 0) {
        countingSortByDigit(arr, exp);
        exp *= 10;
    }
    return arr;
}

function countingSortByDigit(arr, exp) {
    const output = new Array(arr.length);
    const count = new Array(10).fill(0);
    for (let num of arr) count[Math.floor(num / exp) % 10]++;
    for (let i = 1; i < 10; i++) count[i] += count[i - 1];
    for (let i = arr.length - 1; i >= 0; i--) {
        const digit = Math.floor(arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }
    for (let i = 0; i < arr.length; i++) arr[i] = output[i];
}
```

🔹 4. Recursion & Backtracking

Factorial, Fibonacci (recursive vs DP)

N-Queens problem

Rat in a Maze / Backtracking pathfinding

Generate all subsets/permutations

### Factorial, Fibonacci (Recursive vs DP)
Recursion solves problems by breaking into smaller subproblems.

#### Factorial Recursive
```javascript
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

#### Fibonacci Recursive (Inefficient, O(2^n))
```javascript
function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

#### Fibonacci with DP (Memoization, O(n))
```javascript
function fibDP(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    memo[n] = fibDP(n - 1, memo) + fibDP(n - 2, memo);
    return memo[n];
}
```

### N-Queens Problem
Place N queens on an N x N chessboard so no two attack each other. Use backtracking.

```javascript
function solveNQueens(n) {
    const board = Array.from({ length: n }, () => Array(n).fill('.'));
    const result = [];
    backtrack(board, 0, result);
    return result;
}

function backtrack(board, row, result) {
    if (row === board.length) {
        result.push(board.map(r => r.join('')));
        return;
    }
    for (let col = 0; col < board.length; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 'Q';
            backtrack(board, row + 1, result);
            board[row][col] = '.';
        }
    }
}

function isSafe(board, row, col) {
    for (let i = 0; i < row; i++) {
        if (board[i][col] === 'Q') return false;
        if (col - (row - i) >= 0 && board[i][col - (row - i)] === 'Q') return false;
        if (col + (row - i) < board.length && board[i][col + (row - i)] === 'Q') return false;
    }
    return true;
}
```

### Rat in a Maze / Backtracking Pathfinding
Find a path from start to end in a maze using backtracking.

```javascript
function solveMaze(maze) {
    const n = maze.length;
    const path = Array.from({ length: n }, () => Array(n).fill(0));
    if (solveMazeUtil(maze, 0, 0, path)) {
        return path;
    }
    return null;
}

function solveMazeUtil(maze, x, y, path) {
    const n = maze.length;
    if (x === n - 1 && y === n - 1 && maze[x][y] === 1) {
        path[x][y] = 1;
        return true;
    }
    if (isSafeMaze(maze, x, y)) {
        path[x][y] = 1;
        if (solveMazeUtil(maze, x + 1, y, path)) return true;
        if (solveMazeUtil(maze, x, y + 1, path)) return true;
        path[x][y] = 0;
        return false;
    }
    return false;
}

function isSafeMaze(maze, x, y) {
    const n = maze.length;
    return x >= 0 && x < n && y >= 0 && y < n && maze[x][y] === 1;
}
```

### Generate All Subsets/Permutations
#### Subsets (Power Set)
```javascript
function subsets(nums) {
    const result = [];
    backtrackSubsets(nums, 0, [], result);
    return result;
}

function backtrackSubsets(nums, start, current, result) {
    result.push([...current]);
    for (let i = start; i < nums.length; i++) {
        current.push(nums[i]);
        backtrackSubsets(nums, i + 1, current, result);
        current.pop();
    }
}
```

#### Permutations
```javascript
function permute(nums) {
    const result = [];
    backtrackPermute(nums, [], result);
    return result;
}

function backtrackPermute(nums, current, result) {
    if (current.length === nums.length) {
        result.push([...current]);
        return;
    }
    for (let num of nums) {
        if (!current.includes(num)) {
            current.push(num);
            backtrackPermute(nums, current, result);
            current.pop();
        }
    }
}
```

🔹 5. Linked List

Reverse a Linked List (iterative & recursive)

Detect cycle (Floyd’s Cycle Detection)

Merge two sorted linked lists

Remove nth node from end

Find middle node

### Reverse a Linked List
#### Iterative
```javascript
function reverseList(head) {
    let prev = null;
    let curr = head;
    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

#### Recursive
```javascript
function reverseListRecursive(head) {
    if (!head || !head.next) return head;
    const newHead = reverseListRecursive(head.next);
    head.next.next = head;
    head.next = null;
    return newHead;
}
```

### Detect Cycle (Floyd’s Cycle Detection)
Use slow and fast pointers to detect cycle in O(n) time, O(1) space.

```javascript
function hasCycle(head) {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}
```

### Merge Two Sorted Linked Lists
Merge two sorted lists into one sorted list.

```javascript
function mergeTwoLists(l1, l2) {
    const dummy = new ListNode();
    let curr = dummy;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
    }
    curr.next = l1 || l2;
    return dummy.next;
}
```

### Remove Nth Node from End
Use two pointers, fast moves n steps ahead.

```javascript
function removeNthFromEnd(head, n) {
    const dummy = new ListNode(0, head);
    let fast = dummy;
    let slow = dummy;
    for (let i = 0; i < n; i++) {
        fast = fast.next;
    }
    while (fast.next) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return dummy.next;
}
```

### Find Middle Node
Use slow and fast pointers.

```javascript
function middleNode(head) {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
```

🔹 6. Stack & Queue

Implement Stack/Queue using arrays/linked list

Min Stack (stack with O(1) min operation)

Balanced Parentheses (using stack)

LRU Cache (using LinkedHashMap or DLL + HashMap)

Queue using stacks / Stack using queues

### Implement Stack/Queue Using Arrays/Linked List
#### Stack with Array
```javascript
class Stack {
    constructor() {
        this.items = [];
    }
    push(item) { this.items.push(item); }
    pop() { return this.items.pop(); }
    peek() { return this.items[this.items.length - 1]; }
    isEmpty() { return this.items.length === 0; }
}
```

#### Queue with Array
```javascript
class Queue {
    constructor() {
        this.items = [];
    }
    enqueue(item) { this.items.push(item); }
    dequeue() { return this.items.shift(); }
    front() { return this.items[0]; }
    isEmpty() { return this.items.length === 0; }
}
```

### Min Stack
Stack that supports push, pop, top, and getMin in O(1).

```javascript
class MinStack {
    constructor() {
        this.stack = [];
        this.minStack = [];
    }
    push(val) {
        this.stack.push(val);
        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
            this.minStack.push(val);
        }
    }
    pop() {
        if (this.stack.pop() === this.minStack[this.minStack.length - 1]) {
            this.minStack.pop();
        }
    }
    top() { return this.stack[this.stack.length - 1]; }
    getMin() { return this.minStack[this.minStack.length - 1]; }
}
```

### Balanced Parentheses
Use stack to check if parentheses are balanced.

```javascript
function isValid(s) {
    const stack = [];
    const map = { ')': '(', '}': '{', ']': '[' };
    for (let char of s) {
        if (char in map) {
            const top = stack.pop();
            if (top !== map[char]) return false;
        } else {
            stack.push(char);
        }
    }
    return stack.length === 0;
}
```

### LRU Cache
Least Recently Used cache using Map (in JS, Map maintains insertion order).

```javascript
class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.map = new Map();
    }
    get(key) {
        if (!this.map.has(key)) return -1;
        const val = this.map.get(key);
        this.map.delete(key);
        this.map.set(key, val);
        return val;
    }
    put(key, value) {
        if (this.map.has(key)) {
            this.map.delete(key);
        } else if (this.map.size >= this.capacity) {
            const firstKey = this.map.keys().next().value;
            this.map.delete(firstKey);
        }
        this.map.set(key, value);
    }
}
```

### Queue Using Stacks
Implement queue using two stacks.

```javascript
class QueueWithStacks {
    constructor() {
        this.stack1 = [];
        this.stack2 = [];
    }
    enqueue(x) {
        this.stack1.push(x);
    }
    dequeue() {
        if (this.stack2.length === 0) {
            while (this.stack1.length > 0) {
                this.stack2.push(this.stack1.pop());
            }
        }
        return this.stack2.pop();
    }
}
```

🔹 7. Trees

Binary Tree traversals (✅ you asked BFS/DFS)

Lowest Common Ancestor (LCA)

Height / Diameter of tree

Balanced Binary Tree check

Serialize & Deserialize Binary Tree

BST insert, delete, search (✅ BST you asked)

Heap (min-heap / max-heap operations)

### Binary Tree Traversals
#### BFS (Level Order)
```javascript
function levelOrder(root) {
    if (!root) return [];
    const result = [];
    const queue = [root];
    while (queue.length) {
        const level = [];
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            const node = queue.shift();
            level.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(level);
    }
    return result;
}
```

#### DFS: Inorder, Preorder, Postorder
```javascript
function inorderTraversal(root) {
    const result = [];
    function dfs(node) {
        if (!node) return;
        dfs(node.left);
        result.push(node.val);
        dfs(node.right);
    }
    dfs(root);
    return result;
}

function preorderTraversal(root) {
    const result = [];
    function dfs(node) {
        if (!node) return;
        result.push(node.val);
        dfs(node.left);
        dfs(node.right);
    }
    dfs(root);
    return result;
}

function postorderTraversal(root) {
    const result = [];
    function dfs(node) {
        if (!node) return;
        dfs(node.left);
        dfs(node.right);
        result.push(node.val);
    }
    dfs(root);
    return result;
}
```

### Lowest Common Ancestor (LCA)
Find LCA of two nodes in a binary tree.

```javascript
function lowestCommonAncestor(root, p, q) {
    if (!root || root === p || root === q) return root;
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);
    if (left && right) return root;
    return left || right;
}
```

### Height / Diameter of Tree
#### Height
```javascript
function height(root) {
    if (!root) return 0;
    return 1 + Math.max(height(root.left), height(root.right));
}
```

#### Diameter
```javascript
function diameterOfBinaryTree(root) {
    let max = 0;
    function dfs(node) {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        max = Math.max(max, left + right);
        return 1 + Math.max(left, right);
    }
    dfs(root);
    return max;
}
```

### Balanced Binary Tree Check
Check if height difference between subtrees is <=1.

```javascript
function isBalanced(root) {
    function check(node) {
        if (!node) return 0;
        const left = check(node.left);
        const right = check(node.right);
        if (left === -1 || right === -1 || Math.abs(left - right) > 1) return -1;
        return 1 + Math.max(left, right);
    }
    return check(root) !== -1;
}
```

### Serialize & Deserialize Binary Tree
#### Serialize (Preorder)
```javascript
function serialize(root) {
    const result = [];
    function dfs(node) {
        if (!node) {
            result.push('null');
            return;
        }
        result.push(node.val.toString());
        dfs(node.left);
        dfs(node.right);
    }
    dfs(root);
    return result.join(',');
}
```

#### Deserialize
```javascript
function deserialize(data) {
    const vals = data.split(',');
    let i = 0;
    function dfs() {
        if (vals[i] === 'null') {
            i++;
            return null;
        }
        const node = new TreeNode(parseInt(vals[i]));
        i++;
        node.left = dfs();
        node.right = dfs();
        return node;
    }
    return dfs();
}
```

### BST Insert, Delete, Search
#### Search
```javascript
function searchBST(root, val) {
    if (!root || root.val === val) return root;
    return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
}
```

#### Insert
```javascript
function insertIntoBST(root, val) {
    if (!root) return new TreeNode(val);
    if (val < root.val) root.left = insertIntoBST(root.left, val);
    else root.right = insertIntoBST(root.right, val);
    return root;
}
```

#### Delete
```javascript
function deleteNode(root, key) {
    if (!root) return null;
    if (key < root.val) root.left = deleteNode(root.left, key);
    else if (key > root.val) root.right = deleteNode(root.right, key);
    else {
        if (!root.left) return root.right;
        if (!root.right) return root.left;
        const minNode = findMin(root.right);
        root.val = minNode.val;
        root.right = deleteNode(root.right, minNode.val);
    }
    return root;
}

function findMin(node) {
    while (node.left) node = node.left;
    return node;
}
```

### Heap (Min-Heap / Max-Heap Operations)
#### Min-Heap
```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }
    insert(val) {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }
    extractMin() {
        if (this.heap.length === 1) return this.heap.pop();
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.sinkDown(0);
        return min;
    }
    bubbleUp(index) {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.heap[index] >= this.heap[parent]) break;
            [this.heap[index], this.heap[parent]] = [this.heap[parent], this.heap[index]];
            index = parent;
        }
    }
    sinkDown(index) {
        const length = this.heap.length;
        while (true) {
            let left = 2 * index + 1;
            let right = 2 * index + 2;
            let smallest = index;
            if (left < length && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < length && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === index) break;
            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}
```

🔹 8. Graphs

BFS & DFS (✅ covered)

Detect cycle in directed/undirected graph

Topological Sort (DAG)

Dijkstra’s Algorithm (shortest path)

Minimum Spanning Tree (Prim’s/Kruskal’s)

Graph representations: Adjacency List vs Matrix

### BFS & DFS
#### BFS
```javascript
function bfs(graph, start) {
    const visited = new Set();
    const queue = [start];
    visited.add(start);
    const result = [];
    while (queue.length) {
        const node = queue.shift();
        result.push(node);
        for (let neighbor of graph[node]) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    return result;
}
```

#### DFS
```javascript
function dfs(graph, start, visited = new Set(), result = []) {
    visited.add(start);
    result.push(start);
    for (let neighbor of graph[start]) {
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, visited, result);
        }
    }
    return result;
}
```

### Detect Cycle in Undirected Graph
Use DFS or Union-Find.

```javascript
function hasCycleUndirected(graph) {
    const visited = new Set();
    for (let node in graph) {
        if (!visited.has(node)) {
            if (dfsCycle(node, -1, visited, graph)) return true;
        }
    }
    return false;
}

function dfsCycle(node, parent, visited, graph) {
    visited.add(node);
    for (let neighbor of graph[node]) {
        if (!visited.has(neighbor)) {
            if (dfsCycle(neighbor, node, visited, graph)) return true;
        } else if (neighbor !== parent) {
            return true;
        }
    }
    return false;
}
```

### Detect Cycle in Directed Graph
Use DFS with recursion stack.

```javascript
function hasCycleDirected(graph) {
    const visited = new Set();
    const recStack = new Set();
    for (let node in graph) {
        if (dfsCycleDirected(node, visited, recStack, graph)) return true;
    }
    return false;
}

function dfsCycleDirected(node, visited, recStack, graph) {
    visited.add(node);
    recStack.add(node);
    for (let neighbor of graph[node]) {
        if (!visited.has(neighbor) && dfsCycleDirected(neighbor, visited, recStack, graph)) return true;
        else if (recStack.has(neighbor)) return true;
    }
    recStack.delete(node);
    return false;
}
```

### Topological Sort (DAG)
Using Kahn's algorithm (BFS with indegrees).

```javascript
function topologicalSort(graph, indegrees) {
    const queue = [];
    for (let node in indegrees) {
        if (indegrees[node] === 0) queue.push(node);
    }
    const result = [];
    while (queue.length) {
        const node = queue.shift();
        result.push(node);
        for (let neighbor of graph[node]) {
            indegrees[neighbor]--;
            if (indegrees[neighbor] === 0) queue.push(neighbor);
        }
    }
    return result.length === Object.keys(graph).length ? result : [];
}
```

### Dijkstra’s Algorithm
Shortest path in weighted graph with non-negative weights.

```javascript
function dijkstra(graph, start) {
    const distances = {};
    const pq = new PriorityQueue();
    for (let node in graph) {
        distances[node] = Infinity;
    }
    distances[start] = 0;
    pq.enqueue(start, 0);
    while (!pq.isEmpty()) {
        const { node, priority } = pq.dequeue();
        if (priority > distances[node]) continue;
        for (let [neighbor, weight] of graph[node]) {
            const newDist = distances[node] + weight;
            if (newDist < distances[neighbor]) {
                distances[neighbor] = newDist;
                pq.enqueue(neighbor, newDist);
            }
        }
    }
    return distances;
}

// Simple Priority Queue implementation
class PriorityQueue {
    constructor() {
        this.queue = [];
    }
    enqueue(node, priority) {
        this.queue.push({ node, priority });
        this.queue.sort((a, b) => a.priority - b.priority);
    }
    dequeue() {
        return this.queue.shift();
    }
    isEmpty() {
        return this.queue.length === 0;
    }
}
```

### Minimum Spanning Tree (Prim’s/Kruskal’s)
#### Prim’s Algorithm
```javascript
function prims(graph) {
    const n = Object.keys(graph).length;
    const visited = new Set();
    const pq = new PriorityQueue();
    const mst = [];
    pq.enqueue(0, 0); // start from node 0
    while (visited.size < n && !pq.isEmpty()) {
        const { node, priority: weight } = pq.dequeue();
        if (visited.has(node)) continue;
        visited.add(node);
        for (let [neighbor, w] of graph[node]) {
            if (!visited.has(neighbor)) {
                pq.enqueue(neighbor, w);
            }
        }
    }
    // Note: This is simplified; full implementation needs to track edges
    return mst;
}
```

#### Kruskal’s Algorithm (requires Union-Find)
```javascript
function kruskals(edges, n) {
    edges.sort((a, b) => a[2] - b[2]);
    const uf = new UnionFind(n);
    const mst = [];
    for (let [u, v, w] of edges) {
        if (uf.find(u) !== uf.find(v)) {
            uf.union(u, v);
            mst.push([u, v, w]);
        }
    }
    return mst;
}

class UnionFind {
    constructor(size) {
        this.parent = Array.from({ length: size }, (_, i) => i);
        this.rank = Array(size).fill(0);
    }
    find(x) {
        if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }
    union(x, y) {
        const px = this.find(x), py = this.find(y);
        if (px === py) return;
        if (this.rank[px] < this.rank[py]) this.parent[px] = py;
        else if (this.rank[px] > this.rank[py]) this.parent[py] = px;
        else {
            this.parent[py] = px;
            this.rank[px]++;
        }
    }
}
```

### Graph Representations
- **Adjacency List**: Array of lists, space O(V + E), good for sparse graphs.
- **Adjacency Matrix**: 2D array, space O(V^2), good for dense graphs.

```javascript
// Adjacency List
const graphList = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
};

// Adjacency Matrix
const graphMatrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
];
```

🔹 9. Dynamic Programming (DP)

Fibonacci with memoization (basic DP)

Longest Common Subsequence / Substring

Longest Increasing Subsequence

Coin Change problem

0/1 Knapsack

Matrix DP problems (Unique Paths, Min Path Sum)

### Fibonacci with Memoization
```javascript
function fib(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}
```

### Longest Common Subsequence (LCS)
Find length of LCS between two strings.

```javascript
function longestCommonSubsequence(text1, text2) {
    const m = text1.length, n = text2.length;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}
```

### Longest Common Substring
Contiguous substring.

```javascript
function longestCommonSubstring(s1, s2) {
    const m = s1.length, n = s2.length;
    let maxLen = 0;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                maxLen = Math.max(maxLen, dp[i][j]);
            }
        }
    }
    return maxLen;
}
```

### Longest Increasing Subsequence
Length of longest increasing subsequence.

```javascript
function lengthOfLIS(nums) {
    const dp = Array(nums.length).fill(1);
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    return Math.max(...dp);
}
```

### Coin Change Problem
Minimum coins to make amount.

```javascript
function coinChange(coins, amount) {
    const dp = Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    for (let coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
}
```

### 0/1 Knapsack
Max value with weight limit.

```javascript
function knapsack(weights, values, W) {
    const n = weights.length;
    const dp = Array.from({ length: n + 1 }, () => Array(W + 1).fill(0));
    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= W; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][W];
}
```

### Matrix DP Problems
#### Unique Paths
Number of ways to reach bottom-right in grid.

```javascript
function uniquePaths(m, n) {
    const dp = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) dp[i][0] = 1;
    for (let j = 0; j < n; j++) dp[0][j] = 1;
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}
```

#### Min Path Sum
Minimum path sum from top-left to bottom-right.

```javascript
function minPathSum(grid) {
    const m = grid.length, n = grid[0].length;
    const dp = Array.from({ length: m }, () => Array(n).fill(0));
    dp[0][0] = grid[0][0];
    for (let i = 1; i < m; i++) dp[i][0] = dp[i - 1][0] + grid[i][0];
    for (let j = 1; j < n; j++) dp[0][j] = dp[0][j - 1] + grid[0][j];
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
        }
    }
    return dp[m - 1][n - 1];
}
```

🔹 10. Other Must-Know

Hashing (Map & Set complexities ✅ you asked)

Bit Manipulation basics (check odd/even, count set bits, subset generation)

Greedy Algorithms (Activity Selection, Huffman Coding)

Union-Find / Disjoint Set (Kruskal’s, cycle detection)

Trie (Prefix Tree, autocomplete problem)

### Hashing (Map & Set Complexities)
- **HashMap**: Average O(1) for insert, delete, search. Worst O(n).
- **HashSet**: Similar, for unique elements.

In JavaScript, Map and Set have similar complexities.

```javascript
const map = new Map();
map.set('key', 'value'); // O(1) avg
map.get('key'); // O(1) avg
map.delete('key'); // O(1) avg

const set = new Set();
set.add('item'); // O(1) avg
set.has('item'); // O(1) avg
set.delete('item'); // O(1) avg
```

### Bit Manipulation Basics
#### Check Odd/Even
```javascript
function isEven(n) {
    return (n & 1) === 0;
}
```

#### Count Set Bits
```javascript
function countSetBits(n) {
    let count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}
```

#### Subset Generation using Bits
```javascript
function subsets(nums) {
    const result = [];
    const n = nums.length;
    for (let i = 0; i < (1 << n); i++) {
        const subset = [];
        for (let j = 0; j < n; j++) {
            if (i & (1 << j)) subset.push(nums[j]);
        }
        result.push(subset);
    }
    return result;
}
```

### Greedy Algorithms
#### Activity Selection
Select maximum non-overlapping activities.

```javascript
function activitySelection(activities) {
    activities.sort((a, b) => a.end - b.end);
    const result = [activities[0]];
    for (let i = 1; i < activities.length; i++) {
        if (activities[i].start >= result[result.length - 1].end) {
            result.push(activities[i]);
        }
    }
    return result;
}
```

#### Huffman Coding
Build Huffman tree for compression.

```javascript
class HuffmanNode {
    constructor(char, freq) {
        this.char = char;
        this.freq = freq;
        this.left = null;
        this.right = null;
    }
}

function buildHuffmanTree(text) {
    const freq = {};
    for (let char of text) freq[char] = (freq[char] || 0) + 1;
    const pq = Object.entries(freq).map(([char, f]) => new HuffmanNode(char, f));
    pq.sort((a, b) => a.freq - b.freq);
    while (pq.length > 1) {
        const left = pq.shift();
        const right = pq.shift();
        const merged = new HuffmanNode(null, left.freq + right.freq);
        merged.left = left;
        merged.right = right;
        pq.push(merged);
        pq.sort((a, b) => a.freq - b.freq);
    }
    return pq[0];
}
```

### Union-Find / Disjoint Set
For Kruskal’s and cycle detection.

```javascript
class UnionFind {
    constructor(size) {
        this.parent = Array.from({ length: size }, (_, i) => i);
        this.rank = Array(size).fill(0);
    }
    find(x) {
        if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }
    union(x, y) {
        const px = this.find(x), py = this.find(y);
        if (px === py) return false;
        if (this.rank[px] < this.rank[py]) this.parent[px] = py;
        else if (this.rank[px] > this.rank[py]) this.parent[py] = px;
        else {
            this.parent[py] = px;
            this.rank[px]++;
        }
        return true;
    }
}
```

### Trie (Prefix Tree)
For autocomplete and prefix searches.

```javascript
class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }
    insert(word) {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) node.children[char] = new TrieNode();
            node = node.children[char];
        }
        node.isEndOfWord = true;
    }
    search(word) {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) return false;
            node = node.children[char];
        }
        return node.isEndOfWord;
    }
    startsWith(prefix) {
        let node = this.root;
        for (let char of prefix) {
            if (!node.children[char]) return false;
            node = node.children[char];
        }
        return true;
    }
}
```