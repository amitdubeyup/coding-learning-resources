# Data Structures and Algorithms Interview Questions (JavaScript)

This repository contains 200 commonly asked Data Structures and Algorithms questions in technical interviews, implemented in JavaScript. The questions are organized by topics and difficulty levels.

## Table of Contents

1. [Arrays and Strings](#arrays-and-strings)
2. [Linked Lists](#linked-lists)
3. [Stacks and Queues](#stacks-and-queues)
4. [Trees and Graphs](#trees-and-graphs)
5. [Dynamic Programming](#dynamic-programming)
6. [Sorting and Searching](#sorting-and-searching)
7. [Bit Manipulation](#bit-manipulation)
8. [Math and Logic](#math-and-logic)
9. [System Design](#system-design)

## Arrays and Strings

### Easy
1. Two Sum
   ```javascript
   // Example: nums = [2,7,11,15], target = 9
   // Output: [0,1]
   function twoSum(nums, target) {
       const map = new Map();
       for(let i = 0; i < nums.length; i++) {
           const complement = target - nums[i];
           if(map.has(complement)) {
               return [map.get(complement), i];
           }
           map.set(nums[i], i);
       }
       return [];
   }
   ```

2. Valid Parentheses
3. Merge Sorted Array
4. Best Time to Buy and Sell Stock
5. Valid Palindrome
6. Contains Duplicate
7. Remove Duplicates from Sorted Array
8. Single Number
9. Intersection of Two Arrays
10. Move Zeroes

### Medium
11. 3Sum
12. Container With Most Water
13. Group Anagrams
14. Longest Substring Without Repeating Characters
15. Longest Palindromic Substring
16. Product of Array Except Self
17. Spiral Matrix
18. Rotate Image
19. Set Matrix Zeroes
20. Word Search

### Hard
21. Trapping Rain Water
22. Median of Two Sorted Arrays
23. Regular Expression Matching
24. Minimum Window Substring
25. Longest Consecutive Sequence

## Linked Lists

### Easy
26. Reverse Linked List
27. Merge Two Sorted Lists
28. Linked List Cycle
29. Remove Duplicates from Sorted List
30. Palindrome Linked List

### Medium
31. Add Two Numbers
32. Remove Nth Node From End of List
33. Swap Nodes in Pairs
34. Rotate List
35. Copy List with Random Pointer

### Hard
36. Merge K Sorted Lists
37. Reverse Nodes in k-Group
38. LRU Cache
39. LFU Cache
40. Design Linked List

## Stacks and Queues

### Easy
41. Implement Stack using Queues
42. Implement Queue using Stacks
43. Min Stack
44. Valid Parentheses
45. Next Greater Element

### Medium
46. Daily Temperatures
47. Evaluate Reverse Polish Notation
48. Basic Calculator
49. Largest Rectangle in Histogram
50. Sliding Window Maximum

### Hard
51. Maximal Rectangle
52. Trapping Rain Water
53. Longest Valid Parentheses
54. Basic Calculator III
55. Design Circular Queue

## Trees and Graphs

### Easy
56. Maximum Depth of Binary Tree
57. Validate Binary Search Tree
58. Symmetric Tree
59. Binary Tree Level Order Traversal
60. Convert Sorted Array to Binary Search Tree

### Medium
61. Binary Tree Zigzag Level Order Traversal
62. Construct Binary Tree from Preorder and Inorder Traversal
63. Populating Next Right Pointers in Each Node
64. Lowest Common Ancestor of a Binary Tree
65. Binary Tree Maximum Path Sum

### Hard
66. Serialize and Deserialize Binary Tree
67. Word Ladder
68. Word Search II
69. Alien Dictionary
70. Course Schedule

## Dynamic Programming

### Easy
71. Climbing Stairs
72. Best Time to Buy and Sell Stock
73. Maximum Subarray
74. House Robber
75. Min Cost Climbing Stairs

### Medium
76. Longest Increasing Subsequence
77. Coin Change
78. Longest Common Subsequence
79. Word Break
80. Unique Paths

### Hard
81. Edit Distance
82. Regular Expression Matching
83. Wildcard Matching
84. Burst Balloons
85. Super Egg Drop

## Sorting and Searching

### Easy
86. Merge Sorted Array
87. First Bad Version
88. Search Insert Position
89. Squares of a Sorted Array
90. Valid Mountain Array

### Medium
91. Search in Rotated Sorted Array
92. Find First and Last Position of Element in Sorted Array
93. Search a 2D Matrix
94. Kth Largest Element in an Array
95. Top K Frequent Elements

### Hard
96. Median of Two Sorted Arrays
97. Find Minimum in Rotated Sorted Array
98. Count of Smaller Numbers After Self
99. Maximum Gap
100. Sliding Window Median

## Bit Manipulation

### Easy
101. Number of 1 Bits
102. Reverse Bits
103. Single Number
104. Power of Two
105. Counting Bits

### Medium
106. Sum of Two Integers
107. Bitwise AND of Numbers Range
108. Single Number II
109. Single Number III
110. Maximum Product of Word Lengths

### Hard
111. Repeated DNA Sequences
112. Bitwise OR of Subarrays
113. Minimum Number of Flips
114. Maximum XOR of Two Numbers in an Array
115. Find the Duplicate Number

## Math and Logic

### Easy
116. Fizz Buzz
117. Count Primes
118. Power of Three
119. Roman to Integer
120. Happy Number

### Medium
121. Factorial Trailing Zeroes
122. Excel Sheet Column Number
123. Pow(x, n)
124. Sqrt(x)
125. Divide Two Integers

### Hard
126. Basic Calculator
127. Basic Calculator II
128. Basic Calculator III
129. Max Points on a Line
130. Perfect Rectangle

## System Design

### Easy
131. Design Parking System
132. Design HashMap
133. Design HashSet
134. Design Circular Queue
135. Design Browser History

### Medium
136. Design Twitter
137. Design Hit Counter
138. Design Snake Game
139. Design Tic-Tac-Toe
140. Design Phone Directory

### Hard
141. Design Search Autocomplete System
142. Design File System
143. Design In-Memory File System
144. Design Excel Sum Formula
145. Design Log Storage System

## Additional Practice Problems

### Arrays and Strings
146. Longest Common Prefix
147. Valid Anagram
148. First Unique Character in a String
149. Implement strStr()
150. String to Integer (atoi)

### Linked Lists
151. Remove Linked List Elements
152. Odd Even Linked List
153. Split Linked List in Parts
154. Insertion Sort List
155. Sort List

### Trees
156. Binary Tree Paths
157. Sum of Left Leaves
158. Path Sum
159. Path Sum II
160. Binary Tree Right Side View

### Dynamic Programming
161. Maximum Product Subarray
162. House Robber II
163. Best Time to Buy and Sell Stock II
164. Best Time to Buy and Sell Stock III
165. Best Time to Buy and Sell Stock IV

### Graph
166. Number of Islands
167. Surrounded Regions
168. Pacific Atlantic Water Flow
169. Redundant Connection
170. Graph Valid Tree

### Advanced Topics
171. Implement Trie (Prefix Tree)
172. Word Search II
173. Design Add and Search Words Data Structure
174. Word Squares
175. Palindrome Pairs

### System Design
176. Design Rate Limiter
177. Design TinyURL
178. Design Web Crawler
179. Design Distributed Cache
180. Design Distributed Lock

### Additional Challenges
181. Longest Valid Parentheses
182. Trapping Rain Water
183. Largest Rectangle in Histogram
184. Maximal Rectangle
185. Word Ladder II

### Final Practice Set
186. Sliding Window Maximum
187. Minimum Window Substring
188. Longest Substring with At Most K Distinct Characters
189. Longest Substring with At Most Two Distinct Characters
190. Longest Repeating Character Replacement

### Expert Level
191. Alien Dictionary
192. Word Ladder II
193. Word Search II
194. Design Search Autocomplete System
195. Design In-Memory File System

### Final Challenge Set
196. Regular Expression Matching
197. Wildcard Matching
198. Burst Balloons
199. Super Egg Drop
200. Design Excel Sum Formula

## FAANG-Specific Topics

### Advanced System Design
201. Design a Distributed Cache System
202. Design a Rate Limiter
203. Design a Distributed Lock Service
204. Design a Real-time Chat System
205. Design a Distributed Job Scheduler

### Scalability and Performance
206. Design a Scalable Web Crawler
207. Design a Distributed Logging System
208. Design a Real-time Analytics System
209. Design a Distributed File System
210. Design a Load Balancer

### Advanced Data Structures
211. Design a Concurrent HashMap
212. Design a Thread-Safe LRU Cache
213. Design a Distributed Bloom Filter
214. Design a Skip List
215. Design a B+ Tree

### Advanced Algorithms
216. Implement a Distributed Consensus Algorithm
217. Design a Distributed Sorting Algorithm
218. Implement a Distributed Graph Processing System
219. Design a Distributed Search Engine
220. Implement a Distributed Cache Invalidation Strategy

## Company-Specific Focus Areas

### Google
- Graph Algorithms
- String Manipulation
- Dynamic Programming
- System Design
- Scalability

### Amazon
- Object-Oriented Design
- System Design
- Scalability
- Database Design
- API Design

### Meta (Facebook)
- Graph Algorithms
- Dynamic Programming
- System Design
- Scalability
- Real-time Systems

### Apple
- System Design
- Security
- Performance Optimization
- API Design
- Data Structures

### Netflix
- System Design
- Scalability
- Performance
- Distributed Systems
- Real-time Processing

## Advanced Topics for Senior Positions

### System Architecture
221. Design a Microservices Architecture
222. Design a High-Availability System
223. Design a Fault-Tolerant System
224. Design a Scalable Database System
225. Design a Real-time Data Processing Pipeline

### Performance Optimization
226. Design a High-Performance Cache
227. Design a Low-Latency System
228. Design a High-Throughput System
229. Design a Memory-Efficient System
230. Design a CPU-Efficient System

### Security
231. Design a Secure Authentication System
232. Design a Secure Authorization System
233. Design a Secure Data Storage System
234. Design a Secure Communication System
235. Design a Secure API Gateway

## Interview Preparation Strategy

### For FAANG Interviews
1. Focus on:
   - System Design (especially scalability and distributed systems)
   - Advanced Data Structures
   - Complex Algorithm Problems
   - Behavioral Questions
   - Coding Best Practices

2. Practice:
   - Mock Interviews
   - System Design Discussions
   - Code Reviews
   - Performance Optimization
   - Security Considerations

3. Key Areas to Master:
   - Distributed Systems
   - Scalability Patterns
   - Database Design
   - API Design
   - Security Best Practices
   - Performance Optimization
   - Testing Strategies

### Additional Resources
- System Design Primer
- Distributed Systems Concepts
- Scalability Patterns
- Security Best Practices
- Performance Optimization Techniques

## Advanced Implementation Examples

### Distributed Systems
```javascript
// Example: Distributed Cache Implementation
class DistributedCache {
    constructor(nodes) {
        this.nodes = nodes;
        this.consistentHash = new ConsistentHash(nodes);
    }

    async get(key) {
        const node = this.consistentHash.getNode(key);
        return await node.get(key);
    }

    async set(key, value) {
        const node = this.consistentHash.getNode(key);
        return await node.set(key, value);
    }
}
```

### Scalable System Design
```javascript
// Example: Load Balancer Implementation
class LoadBalancer {
    constructor(servers) {
        this.servers = servers;
        this.currentIndex = 0;
    }

    getNextServer() {
        const server = this.servers[this.currentIndex];
        this.currentIndex = (this.currentIndex + 1) % this.servers.length;
        return server;
    }

    async handleRequest(request) {
        const server = this.getNextServer();
        return await server.process(request);
    }
}
```

## Final Tips for FAANG Interviews

1. System Design Focus:
   - Always consider scalability
   - Think about distributed systems
   - Consider failure scenarios
   - Plan for monitoring and logging
   - Design for security

2. Coding Best Practices:
   - Write clean, maintainable code
   - Consider edge cases
   - Optimize for performance
   - Include proper error handling
   - Add comprehensive tests

3. Problem-Solving Approach:
   - Clarify requirements
   - Consider multiple solutions
   - Discuss trade-offs
   - Implement optimal solution
   - Test thoroughly

4. Communication:
   - Explain your thought process
   - Ask clarifying questions
   - Discuss alternatives
   - Consider feedback
   - Show enthusiasm

Remember: FAANG interviews often focus on system design, scalability, and real-world problem-solving. Practice these aspects extensively along with the algorithmic problems.

## How to Use This Repository

1. Each problem includes:
   - Problem statement
   - Example inputs and outputs
   - Solution approach
   - JavaScript implementation
   - Time and space complexity analysis

2. Practice Strategy:
   - Start with Easy problems in each category
   - Move to Medium problems once comfortable
   - Attempt Hard problems after mastering Medium
   - Focus on understanding patterns and approaches
   - Practice implementing solutions from scratch

3. Tips for Interview Preparation:
   - Understand the problem thoroughly before coding
   - Consider edge cases
   - Write clean, readable code
   - Explain your thought process
   - Optimize your solution

## Contributing

Feel free to contribute by:
- Adding new problems
- Improving existing solutions
- Adding more detailed explanations
- Suggesting optimizations
- Adding test cases

## License

This project is licensed under the MIT License - see the LICENSE file for details.
