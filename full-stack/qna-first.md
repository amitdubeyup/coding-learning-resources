# Interview Answers

## Question 1: Introduce yourself?

**Answer:** Hi, I'm Amit Dubey. I've been working as a Full Stack Engineer for about 8 years. On the frontend, I mainly work with HTML, CSS, JavaScript, and React, while on the backend I focus on Node.js and Express.js. I also have hands-on experience with databases like MySQL and MongoDB. That's a quick overview of my technical background. I'd be happy to walk you through my projects and the companies I've worked with in more detail if you'd like.

## Question 2: Explain your recent project?

**Answer:** In my recent project at HireEZ, I worked on a recruitment platform that helps companies source candidates—somewhat similar to a job board, but designed specifically for B2B businesses. The platform has multiple in-house modules, such as:

- Sourcing – for finding and sourcing candidates,
- Talent Pool – to maintain pools of potential candidates for future hiring,
- Engagement – to reach out and interact with candidates,
- Applicant Match – which works like an ATS to match candidates with job descriptions, and
- Insights – to provide detailed company and talent demographics.

I contributed to several key modules, including Sourcing, Talent Pool, Insights, and the Customer Onboarding journey. My work mainly focused on building scalable features, improving user workflows, and ensuring smooth integration across these modules.

## Question 3: Explain your recent project and the challenges?

**Answer:** In my recent project at HireEZ, I worked on managing and enriching a large talent pool of over 80 million candidates. We continuously pull candidate data from 10+ public sources such as LinkedIn, GitHub, Stack Overflow, Glassdoor, and Medium.

The main challenge we faced was that the data came in unstructured and inconsistent formats, since every source had its own schema and often changed over time. To handle this, we built a custom rule engine using Python (with Pandas) combined with LLM-based logic to transform and normalize the data into a consistent format.

Another challenge was handling updates: when new candidates were added, we had to insert them into the database, while for existing ones we needed to patch and merge their profiles without introducing duplicates. Our cron jobs, which run frequently, are responsible for pulling, transforming, and updating this data.

Overall, the biggest challenges were data normalization, adapting quickly to changing external data formats, and ensuring database consistency at scale, which we solved through automation and continuous monitoring.

## Question 4: How do you collaborate with team members?

**Answer:** Collaboration really depends on the work culture—onsite, hybrid, or remote—and I've had the opportunity to work in all three setups.

In a remote or hybrid environment, we typically follow Agile practices like daily stand-ups, sprint planning, and retrospectives. We use tools like Jira for task tracking, Slack or Microsoft Teams for quick communication, and group calls or 1:1s when deeper discussions are needed. For documentation and knowledge sharing, we maintain Confluence or shared docs, which ensures everyone stays aligned.

In an onsite setting, much of the collaboration happens in person—daily stand-ups, whiteboard discussions, or quick syncs at the desk. But even there, we still rely on Jira for task tracking and Slack/email for written communication to maintain transparency and a record of decisions.

For approvals, priorities, or escalations, I prefer to document things clearly over email or project management tools, so there's visibility and accountability.

I also believe in best practices like clear ownership of tasks, regular knowledge sharing, code reviews, and open communication, which help the team stay productive and collaborative regardless of the work setup.

## Question 5: Roles and responsibilities?

**Answer:** My key roles and responsibilities primarily revolve around the end-to-end design and development of modules, covering the frontend, backend, and database layers. This includes both architecture planning and hands-on coding, since as a full stack engineer, I take full ownership of the modules I work on.

In addition to individual modules, I also contribute to shared components and cross-team projects, ensuring consistency and reusability across the system.

Beyond coding, my responsibilities extend to:

- Creating technical design documents and development plans for better clarity and alignment.
- Collaborating with stakeholders, project managers, and QA engineers to refine requirements and ensure delivery quality.
- Conducting code reviews and promoting best practices like clean code, SOLID principles, and performance optimization.
- Participating in team discussions on technical strategies, timelines, and resource planning.

I follow Agile practices—including sprint planning, daily stand-ups, and retrospectives—which ensure continuous collaboration, faster feedback loops, and better delivery.

Overall, I see my role as not just delivering code, but also ensuring scalability, maintainability, and collaboration across the project lifecycle.

## Question 6: Mention a project in which you feel proud of yourself?

**Answer:** One project I feel particularly proud of was the Loan Management System I worked on at Arthmate. When I joined, I was assigned a critical module with complete ownership. The system at that time struggled with handling high request volumes, peak loads, failures, and lacked proper monitoring.

My first step was to review the existing architecture and identify bottlenecks. I then prepared a detailed improvement plan with clear metrics on scalability, fault tolerance, and performance, and discussed it with my manager for alignment.

Once approved, I redesigned the system by decoupling the monolithic application into microservices. For example:

- A dedicated microservice for third-party API calls,
- A microservice for bulk operations, and
- A communication service for notifications, emails, SMS, and WhatsApp messages.

To achieve reliability and scalability, I implemented a messaging queue and event-driven architecture, which improved throughput and fault isolation. I also integrated proper logging, monitoring, and alerting mechanisms to ensure proactive issue detection.

When the new system went live, it handled peak loads seamlessly and reduced failures significantly. The entire organization appreciated the impact, and that recognition made me proud.

At the same time, I believe success isn't about one milestone—it's about being consistent, following best practices, and continuously improving systems to deliver long-term value.

## Question 7: Time & space complexity?

**Answer:**

### Time Complexity

1. **Loops**
   - Single loop → O(n)
   - Nested loops → Multiply → O(n²), O(n³)
   - Logarithmic loop (i *= 2) → O(log n)

2. **Sequential Statements**
   - Add complexities, then keep dominant term
   - Example: O(n) + O(n²) = O(n²)

3. **Recursion**
   - Express as recurrence relation
   - Example: Merge Sort → T(n) = 2T(n/2) + O(n) → O(n log n)
   - Common patterns:
     - Function calls itself once per step → O(n)
     - Branches into 2 calls → O(2ⁿ)
     - Divides problem in half → O(log n)

4. **Sorting Complexities**
   - Efficient sorting (Merge Sort, Quick Sort) → O(n log n)
   - Simple sorting (Bubble, Selection, Insertion) → O(n²)

5. **Ignore Constants**
   - O(2n) → O(n)
   - O(5n² + 3n + 10) → O(n²)

### Space Complexity

- Fixed part → constants, primitive variables → O(1)
- Auxiliary data structures → arrays, maps, sets, etc. → O(n), O(n²)
- Recursion stack → depends on depth of recursion → O(n) (e.g., factorial, DFS)

## Question 8: Find the second largest number in an array and explain the approach with time and space complexities.

**Answer:** Sure, I'll walk you through both the brute-force and the optimal solutions.

### 1. Brute Force Approach

**Idea:** Sort the array, then pick the second largest element from the end.

**Steps:**
- Sort the array in ascending order.
- Traverse from the end to find the first element smaller than the maximum (to handle duplicates).
- Return that as the second largest.

**Time Complexity:**
- Sorting takes O(n log n).
- Traversing from the end is O(n) in the worst case.
- So total → O(n log n).

**Space Complexity:**
- If using an in-place sort like quicksort → O(1) (ignoring recursion stack).
- If not in-place → O(n).

This works but is not efficient because we don't really need the full sorting just to find the second largest.

### 2. Optimal Approach (Single Pass)

**Idea:** Track the largest and second largest in a single scan.

**Steps:**
- Initialize two variables: first = -∞, second = -∞.
- Traverse the array:
  - If current element > first: update second = first, then first = current.
  - Else if current element > second and current element != first: update second = current.
- At the end, second holds the second largest element.

**Time Complexity:**
- Single pass → O(n).

**Space Complexity:**
- Just two variables → O(1).

This is clearly more efficient than sorting because it avoids unnecessary work.

**Edge Cases to Handle:**
- If array has fewer than 2 distinct elements, return something like None or an error.
- Works with negative numbers as well.

**Why Optimal is Better?**
- Sorting is overkill when you only need one element.
- With O(n) time and O(1) space, the single-pass approach is the most efficient solution.

## Question 9: What is a Palindrome? Explain in details with time & space complexity?

**Answer:** A palindrome is a string, number, or sequence that reads the same forward and backward.

**Examples:**
- ✅ Palindromes: "madam", "racecar", "121", "abba"
- ❌ Non-palindromes: "hello", "abc"

### Approach to Check a Palindrome

#### 1. Brute Force Approach

Reverse the string and compare it with the original.

**Example:**

```javascript
function isPalindrome(str) {
  let reversed = str.split("").reverse().join("");
  return str === reversed;
}
```

**Time Complexity:**
- Splitting: O(n)
- Reversing: O(n)
- Joining: O(n)
- Comparison: O(n)
- Total = O(n)

**Space Complexity:**
- Extra space for reversed string → O(n)

#### 2. Optimal Approach (Two-Pointer Technique)

Use two pointers:
- One starts at the beginning (left)
- One starts at the end (right)
- Move inward, comparing characters.
- If all match → palindrome.

**Example:**

```javascript
function isPalindrome(str) {
  let left = 0, right = str.length - 1;
  
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}
```

**Time Complexity:**
- Each character is compared once → O(n)

**Space Complexity:**
- Only uses a few variables → O(1) (constant space)

#### 3. Palindrome for Numbers

Convert number to string and use same approach OR reverse the number mathematically.

**Example (number check without string conversion):**

```javascript
function isPalindromeNumber(num) {
  if (num < 0) return false; // negatives not palindrome
  let original = num, reversed = 0;
  
  while (num > 0) {
    let digit = num % 10;
    reversed = reversed * 10 + digit;
    num = Math.floor(num / 10);
  }
  
  return original === reversed;
}
```

**Time Complexity:**
- Iterates through digits → O(log₁₀(n)) (since number of digits = log₁₀(n))

**Space Complexity:**
- Uses only variables → O(1)

**Summary:**
- Brute force string reverse: O(n) time, O(n) space
- Two-pointer optimal: O(n) time, O(1) space
- Number palindrome: O(log n) time, O(1) space

## Question 10: What is Tree, Types of Tree?

**Answer:** A Tree is a non-linear data structure that organizes data in a hierarchical manner. It consists of:

- Nodes → represent data.
- Edges → represent connections between nodes.
- Root Node → the topmost node.
- Parent & Child → relationship between connected nodes.
- Leaf Nodes → nodes with no children.

Unlike arrays or linked lists (linear structures), trees are useful for representing hierarchies, like file systems, organizational charts, or XML/HTML documents.

### Types of Trees

1. **General Tree**
   - No restriction on number of children a node can have.

2. **Binary Tree**
   - Each node has at most 2 children (left & right).

3. **Full Binary Tree**
   - Every node has either 0 or 2 children.

4. **Complete Binary Tree**
   - All levels are completely filled except possibly the last, which is filled left to right.

5. **Perfect Binary Tree**
   - All internal nodes have 2 children, and all leaf nodes are at the same level.

6. **Balanced Binary Tree**
   - The height difference between left and right subtrees is at most 1. (e.g., AVL Tree, Red-Black Tree).

7. **Binary Search Tree (BST)**
   - Left child < Parent < Right child.
   - Used for fast searching, insertion, and deletion.

8. **AVL Tree**
   - A self-balancing BST, where balance factor (left height – right height) is always -1, 0, or +1.

9. **Red-Black Tree**
   - A self-balancing BST used in maps/sets (Java, C++ STL). Ensures O(log n) operations.

10. **N-ary Tree**
    - Each node can have at most N children (generalization of binary tree).

11. **Trie (Prefix Tree)**
    - Specialized tree used for storing strings or prefixes efficiently (used in autocomplete, spell-checkers).

12. **Heap Tree**
    - A complete binary tree where parent satisfies heap property:
      - Max Heap → Parent ≥ children
      - Min Heap → Parent ≤ children

## Question 11: What is Graph, Types of Graph?

**Answer:** A Graph is a non-linear data structure consisting of:

- Vertices (Nodes) → represent entities.
- Edges (Connections) → represent relationships between entities.

Graphs are widely used to model real-world problems like social networks (friends as nodes, relationships as edges), maps (cities as nodes, roads as edges), and computer networks.

### Types of Graphs

#### 1. Based on Edges Direction
- **Undirected Graph** → edges have no direction (friendship in social networks).
- **Directed Graph (Digraph)** → edges have direction (follows on Twitter).

#### 2. Based on Edge Weights
- **Unweighted Graph** → edges have no weight.
- **Weighted Graph** → edges have weights (like distance, cost, time).

#### 3. Based on Connectivity
- **Connected Graph** → there is a path between every pair of vertices.
- **Disconnected Graph** → some vertices are isolated.

#### 4. Special Types
- **Cyclic Graph** → contains at least one cycle.
- **Acyclic Graph** → no cycles.
- **DAG (Directed Acyclic Graph)** → important in scheduling, dependency resolution.
- **Complete Graph (Kn)** → every vertex is connected to every other vertex.
- **Sparse Graph** → few edges compared to vertices.
- **Dense Graph** → edges are close to maximum possible.

#### 5. Tree vs Graph
A Tree is a special case of a graph:
- Connected
- Acyclic
- N nodes with N-1 edges

## Question 12: What is BST, BFS & DFS traversal along with time & space complexity in details?

**Answer:** A Binary Search Tree (BST) is a special type of binary tree with the following property:

- Left child < Parent < Right child.

This allows efficient searching, insertion, and deletion in O(log n) (if balanced).

If not balanced (e.g., skewed tree), worst-case time complexity becomes O(n).

### Tree Traversals

Traversal = visiting all nodes of a tree in a systematic order. The two most common traversal strategies are:

#### BFS (Breadth-First Search / Level Order Traversal)

Traverses the tree level by level (root → children → grandchildren).

Implemented using a Queue (FIFO).

**Example:**

```
      10
     /  \
    6    15
   / \     \
  3   8     20
BFS Order: 10 → 6 → 15 → 3 → 8 → 20
```

**Time Complexity:**
- Visits each node once → O(n)

**Space Complexity:**
- Queue stores nodes → O(w) where w = max width of tree.
- Worst case (complete binary tree) → O(n)

#### DFS (Depth-First Search Traversal)

DFS explores as far as possible along one branch before backtracking.
Implemented using Recursion (stack) or explicit stack.

**Types of DFS:**

- **Inorder (Left → Root → Right)**
  - For BST, gives sorted order of values.
  - Example: 3 → 6 → 8 → 10 → 15 → 20

- **Preorder (Root → Left → Right)**
  - Used for tree construction/serialization.
  - Example: 10 → 6 → 3 → 8 → 15 → 20

- **Postorder (Left → Right → Root)**
  - Used for deleting/freeing tree.
  - Example: 3 → 8 → 6 → 20 → 15 → 10

**Time Complexity:**
- Visits each node once → O(n)

**Space Complexity:**
- Recursive stack depth = height of tree = O(h)
- Balanced tree → O(log n)
- Skewed tree → O(n)

### Summary Table

| Traversal | Data Structure Used | Time Complexity | Space Complexity | Use Case |
|-----------|---------------------|-----------------|------------------|----------|
| BFS | Queue | O(n) | O(n) (worst) | Shortest path in unweighted graph, level order |
| DFS | Stack/Recursion | O(n) | O(h) | Search, tree construction, expression trees |

