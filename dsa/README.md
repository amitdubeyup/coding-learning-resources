# Data Structures & Algorithms — the pattern-based way

The fastest way to pass DSA rounds is **not** grinding 500 random problems. It's
learning ~15 recurring *patterns*, because almost every interview problem is one
of these patterns wearing a costume. Learn to recognize the pattern in the first
2 minutes and the code writes itself.

This guide is language-agnostic; templates are in Python (the interview default).

## Contents
- [How to actually prepare](#how-to-actually-prepare)
- [Complexity you must know cold](#complexity-you-must-know-cold)
- [The 15 patterns](#the-15-patterns) — with templates + signature problems
- [Data structure cheat sheet](#data-structure-cheat-sheet)
- [A 6-week study plan](#a-6-week-study-plan)
- [The 45-minute interview loop](#the-45-minute-interview-loop)
- [Companion files](#companion-files)

---

## How to actually prepare

1. **Learn the pattern before the problems.** Read the pattern, type the
   template from memory, then solve its 3–5 signature problems.
2. **Solve, don't read.** Reading solutions builds false confidence. Write code.
3. **Redo misses after 3 days.** Spaced repetition is what makes patterns stick.
4. **Always narrate:** clarify → brute force + its Big-O → optimize → code →
   test with edge cases. Silent coding fails senior loops even when the code works.

---

## Complexity you must know cold

| Structure / op | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array (by index) | O(1) | O(n) | O(n) | O(n) |
| Dynamic array (append) | O(1) | O(n) | O(1)* | O(n) |
| Hash map / set | — | O(1)* | O(1)* | O(1)* |
| Balanced BST / sorted map | O(log n) | O(log n) | O(log n) | O(log n) |
| Binary heap | O(1) peek | O(n) | O(log n) | O(log n) |
| Linked list | O(n) | O(n) | O(1)** | O(1)** |

\* amortized / average · \** given the node reference

**Sorting:** comparison sorts are Θ(n log n) lower bound. Know that quicksort is
O(n²) worst case but fast in practice, mergesort is stable O(n log n) with O(n)
space, and counting/radix sort beat n log n only for bounded integer keys.

**Rules of thumb by input size:** n ≤ 20 → exponential/backtracking is fine;
n ≤ 3,000 → O(n²) ok; n ≤ 10⁶ → need O(n) or O(n log n); n huge → O(log n) or O(1).

---

## The 15 patterns

Each pattern lists **when to reach for it**, a **template**, and **signature
problems** (search the exact title on any judge).

### 1. Two pointers
**When:** sorted array/string; find a pair/triplet; compare from both ends.
```python
def two_sum_sorted(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return [lo, hi]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []
```
**Signature:** Two Sum II, 3Sum, Container With Most Water, Valid Palindrome, Trapping Rain Water.

### 2. Sliding window
**When:** longest/shortest/optimal *contiguous* subarray or substring.
```python
def longest_unique(s):
    seen, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```
**Signature:** Longest Substring Without Repeating Characters, Minimum Window Substring, Longest Repeating Character Replacement, Max Sum Subarray of Size K.

### 3. Fast & slow pointers
**When:** cycle detection, find middle, linked-list "meeting point" problems.
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```
**Signature:** Linked List Cycle I/II, Middle of the Linked List, Happy Number, Find the Duplicate Number.

### 4. Merge intervals
**When:** overlapping ranges — merge, insert, or count.
```python
def merge(intervals):
    intervals.sort()
    out = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
```
**Signature:** Merge Intervals, Insert Interval, Meeting Rooms I/II, Non-overlapping Intervals.

### 5. Cyclic sort
**When:** array of numbers in a known range `1..n`; find missing/duplicate in O(n)/O(1).
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums
```
**Signature:** Missing Number, Find All Numbers Disappeared in an Array, Find the Duplicate Number, First Missing Positive.

### 6. In-place linked-list reversal
**When:** reverse all or part of a linked list without extra space.
```python
def reverse(head):
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
```
**Signature:** Reverse Linked List, Reverse Linked List II, Reverse Nodes in k-Group, Swap Nodes in Pairs.

### 7. BFS (level-order)
**When:** shortest path in an unweighted graph/grid; process a tree level by level.
```python
from collections import deque

def bfs(root):
    q, out = deque([root] if root else []), []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            q.extend(c for c in (node.left, node.right) if c)
        out.append(level)
    return out
```
**Signature:** Binary Tree Level Order Traversal, Word Ladder, Rotting Oranges, Shortest Path in Binary Matrix.

### 8. DFS / backtracking
**When:** explore all paths; generate combinations/permutations/subsets; tree path sums.
```python
def subsets(nums):
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res
```
**Signature:** Subsets, Permutations, Combination Sum, Word Search, N-Queens, Path Sum II.

### 9. Heap / top-K
**When:** k largest/smallest/most-frequent; streaming medians; merge k sorted lists.
```python
import heapq

def top_k_frequent(nums, k):
    from collections import Counter
    return [x for x, _ in Counter(nums).most_common(k)]

def k_largest(nums, k):
    return heapq.nlargest(k, nums)
```
**Signature:** Top K Frequent Elements, Kth Largest Element, Merge k Sorted Lists, Find Median from Data Stream (two heaps).

### 10. Modified binary search
**When:** sorted (or rotated-sorted) input; "find boundary/first/last"; monotonic answer space.
```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:               # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                    # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```
**Signature:** Search in Rotated Sorted Array, Find First/Last Position, Koko Eating Bananas, Median of Two Sorted Arrays.

### 11. Dynamic programming
**When:** overlapping subproblems + optimal substructure ("count ways", "min/max cost", "can we").
Approach: define the state, write the recurrence, memoize (top-down), then optionally tabulate (bottom-up).
```python
def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
**Signature:** Climbing Stairs, House Robber, Coin Change, Longest Common Subsequence, Longest Increasing Subsequence, Edit Distance, 0/1 Knapsack, Word Break.

### 12. Greedy
**When:** a locally optimal choice provably leads to the global optimum (interval scheduling, jumps).
```python
def can_jump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True
```
**Signature:** Jump Game I/II, Gas Station, Task Scheduler, Partition Labels.

### 13. Topological sort
**When:** dependency ordering on a DAG (course schedules, build order).
```python
from collections import deque, defaultdict

def topo(n, edges):
    g, indeg = defaultdict(list), [0] * n
    for u, v in edges:            # u -> v
        g[u].append(v); indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # empty => cycle
```
**Signature:** Course Schedule I/II, Alien Dictionary, Minimum Height Trees.

### 14. Union-Find (disjoint set)
**When:** connectivity, grouping, cycle detection in an undirected graph.
```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n)); self.r = [0] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]      # path compression
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.r[ra] += self.r[ra] == self.r[rb]
        return True
```
**Signature:** Number of Provinces, Redundant Connection, Accounts Merge, Graph Valid Tree.

### 15. Trie (prefix tree)
**When:** prefix search, autocomplete, word dictionaries, multi-word grid search.
```python
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True
    def search(self, word, prefix=False):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return True if prefix else '$' in node
```
**Signature:** Implement Trie, Word Search II, Design Add and Search Words, Replace Words.

> **Bit manipulation** is a mini-pattern worth 30 minutes: XOR to cancel pairs
> (Single Number), `n & (n-1)` to drop the lowest set bit (Number of 1 Bits,
> Counting Bits), and masks for subsets.

---

## Data structure cheat sheet

Choose by the operation you need most:
- **Need O(1) lookup by key** → hash map/set.
- **Need order + range queries** → sorted structure / balanced BST.
- **Need repeated min/max** → heap.
- **Need LIFO/most-recent** → stack (monotonic stack for "next greater/smaller").
- **Need FIFO / BFS** → queue / deque.
- **Need prefix matching** → trie.
- **Need connectivity/grouping** → union-find.

---

## A 6-week study plan

- **Week 1:** Big-O, arrays/strings, hash maps · patterns 1–2 (two pointers, sliding window).
- **Week 2:** linked lists, stacks/queues · patterns 3, 6, monotonic stack.
- **Week 3:** trees + BFS/DFS · patterns 7–8.
- **Week 4:** heaps, binary search, intervals · patterns 4, 9, 10.
- **Week 5:** graphs · patterns 13–15 + graph BFS/DFS.
- **Week 6:** dynamic programming + greedy · patterns 11–12; timed mock interviews.

Target ~6–8 problems per pattern (easy → medium → 1–2 hard). Depth beats volume.

---

## The 45-minute interview loop

1. **Clarify (2–3 min):** inputs, ranges, duplicates, empty/one-element cases, expected output.
2. **Brute force (2 min):** state it *and its Big-O* out loud — shows structure.
3. **Optimize:** name the pattern; explain why it lowers the complexity.
4. **Code (15–20 min):** clean names, talk as you type.
5. **Test:** dry-run a normal case + edge cases (empty, single, max, negatives, duplicates).
6. **Analyze:** final time/space; mention one further optimization or trade-off.

---

## Companion files

- [`sorting.md`](sorting.md) — sorting algorithms **plus a senior "what's actually
  tested" lens**: the JS comparator gotcha, quicksort/mergesort/heapsort trade-offs,
  stability, quickselect for top-K, and when non-comparison sorts apply.
- [`trees-and-graphs.md`](trees-and-graphs.md) — tree/graph structures and traversals,
  **with the graph algorithms interviews expect** (topological sort, Union-Find,
  Dijkstra) and the high-frequency tree problems (validate BST, LCA, diameter,
  serialize).
- [`coding-problems-100.md`](coding-problems-100.md) — 100 easy/medium warm-up programs
  for language fluency. Treat these as **fundamentals, not FAANG-level**: for FAANG,
  apply the 15 patterns above to medium/hard problems.
- [`common-topics-qa.md`](common-topics-qa.md) — a topic-by-topic DSA Q&A refresher
  (complexity, arrays/strings, and more) — good for quick concept review alongside the
  patterns above.
