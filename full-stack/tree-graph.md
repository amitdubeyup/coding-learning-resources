# Data Structures: Trees and Graphs

This document covers fundamental data structures including Trees, Graphs, Binary Trees, Binary Search Trees, and traversal algorithms BFS and DFS. Each section includes detailed explanations, time and space complexities, working principles, and basic JavaScript implementations.

## Table of Contents

- [Trees and Graphs](#trees-and-graphs)
- [Binary Tree and Binary Search Tree](#binary-tree-and-binary-search-tree)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)

## Trees and Graphs

### Trees

A tree is a hierarchical data structure consisting of nodes connected by edges. It has the following properties:
- One root node
- Each node has zero or more child nodes
- No cycles (acyclic)
- Connected (all nodes are reachable from the root)

### Graphs

A graph is a non-hierarchical data structure consisting of vertices (nodes) connected by edges. It can be:
- **Directed**: Edges have direction
- **Undirected**: Edges have no direction
- **Weighted**: Edges have weights/costs
- **Unweighted**: Edges have no weights

### Time Complexity
- **Tree Operations**: Varies by operation (O(1) to O(n))
- **Graph Operations**: Varies by representation and operation

### Space Complexity
- **Adjacency Matrix**: O(V²) where V is number of vertices
- **Adjacency List**: O(V + E) where E is number of edges

### How They Work
Trees are used for hierarchical data representation (file systems, organization charts). Graphs are used for modeling relationships (social networks, maps, web pages).

### Basic JavaScript Implementation

#### Tree Node
```javascript
class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }

    addChild(node) {
        this.children.push(node);
    }
}
```

#### Graph (Adjacency List)
```javascript
class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }

    addEdge(vertex1, vertex2) {
        this.addVertex(vertex1);
        this.addVertex(vertex2);
        this.adjacencyList[vertex1].push(vertex2);
        this.adjacencyList[vertex2].push(vertex1); // For undirected graph
    }
}
```

## Binary Tree and Binary Search Tree

### Binary Tree

A binary tree is a tree data structure where each node has at most two children, referred to as the left and right child.

### Binary Search Tree (BST)

A BST is a binary tree with the following properties:
- Left subtree of a node contains only nodes with values less than the node's value
- Right subtree contains only nodes with values greater than the node's value
- Both left and right subtrees are also BSTs
- No duplicate values (typically)

### Time Complexity
- **Binary Tree Operations**:
  - Search: O(n) worst case, O(log n) average
  - Insert: O(n) worst case, O(log n) average
  - Delete: O(n) worst case, O(log n) average
- **BST Operations**:
  - Search: O(h) where h is height (O(log n) for balanced, O(n) for skewed)
  - Insert: O(h)
  - Delete: O(h)

### Space Complexity
- O(n) for storing n nodes

### How They Work

Binary trees provide efficient search and sorting operations when balanced. BSTs maintain sorted order, allowing for fast lookups, insertions, and deletions. The efficiency depends on the tree's balance - a balanced BST provides O(log n) operations, while a skewed tree degrades to O(n).

### Basic JavaScript Implementation

#### Binary Tree Node
```javascript
class BinaryTreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
```

#### Binary Search Tree
```javascript
class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(value) {
        const newNode = new BinaryTreeNode(value);
        if (!this.root) {
            this.root = newNode;
            return this;
        }

        let current = this.root;
        while (true) {
            if (value < current.value) {
                if (!current.left) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else if (value > current.value) {
                if (!current.right) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            } else {
                // Duplicate values not allowed
                return this;
            }
        }
    }

    search(value) {
        let current = this.root;
        while (current) {
            if (value < current.value) {
                current = current.left;
            } else if (value > current.value) {
                current = current.right;
            } else {
                return true;
            }
        }
        return false;
    }

    // In-order traversal (left, root, right) - gives sorted order
    inOrderTraversal(node = this.root, result = []) {
        if (node) {
            this.inOrderTraversal(node.left, result);
            result.push(node.value);
            this.inOrderTraversal(node.right, result);
        }
        return result;
    }
}
```

## Breadth-First Search (BFS)

BFS is a graph traversal algorithm that explores all vertices at the present depth level before moving to the next depth level. It uses a queue data structure.

### Time Complexity
- O(V + E) where V is vertices and E is edges
- Each vertex and edge is visited once

### Space Complexity
- O(V) for the queue in worst case (when graph is dense)

### How It Works
1. Start from a source vertex
2. Visit all its adjacent vertices
3. Mark visited vertices to avoid cycles
4. Use a queue: enqueue visited vertices, dequeue to process
5. Process level by level

BFS is useful for finding shortest paths in unweighted graphs, level-order traversal in trees, and solving puzzles like mazes.

### Basic JavaScript Implementation
```javascript
function bfs(graph, startVertex) {
    const visited = new Set();
    const queue = [];
    const result = [];

    visited.add(startVertex);
    queue.push(startVertex);

    while (queue.length > 0) {
        const currentVertex = queue.shift();
        result.push(currentVertex);

        // Visit all adjacent vertices
        for (const neighbor of graph.adjacencyList[currentVertex] || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }

    return result;
}

// Usage with Graph class from earlier
const graph = new Graph();
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('B', 'D');
graph.addEdge('C', 'E');

console.log(bfs(graph, 'A')); // ['A', 'B', 'C', 'D', 'E']
```

## Depth-First Search (DFS)

DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack data structure (or recursion).

### Time Complexity
- O(V + E) where V is vertices and E is edges
- Each vertex and edge is visited once

### Space Complexity
- O(V) for the recursion stack in worst case
- O(h) where h is the maximum depth of the graph/tree

### How It Works
1. Start from a source vertex
2. Explore as deep as possible along one path
3. Backtrack when no unvisited adjacent vertices remain
4. Use recursion or a stack to keep track of vertices
5. Mark visited vertices to avoid cycles

DFS is useful for topological sorting, detecting cycles, solving puzzles, and path finding in mazes.

### Basic JavaScript Implementation

#### Recursive DFS
```javascript
function dfsRecursive(graph, startVertex, visited = new Set(), result = []) {
    visited.add(startVertex);
    result.push(startVertex);

    for (const neighbor of graph.adjacencyList[startVertex] || []) {
        if (!visited.has(neighbor)) {
            dfsRecursive(graph, neighbor, visited, result);
        }
    }

    return result;
}

// Usage
console.log(dfsRecursive(graph, 'A')); // ['A', 'B', 'D', 'C', 'E']
```

#### Iterative DFS (using stack)
```javascript
function dfsIterative(graph, startVertex) {
    const visited = new Set();
    const stack = [];
    const result = [];

    stack.push(startVertex);

    while (stack.length > 0) {
        const currentVertex = stack.pop();

        if (!visited.has(currentVertex)) {
            visited.add(currentVertex);
            result.push(currentVertex);

            // Push neighbors in reverse order to maintain order
            const neighbors = graph.adjacencyList[currentVertex] || [];
            for (let i = neighbors.length - 1; i >= 0; i--) {
                if (!visited.has(neighbors[i])) {
                    stack.push(neighbors[i]);
                }
            }
        }
    }

    return result;
}

// Usage
console.log(dfsIterative(graph, 'A')); // ['A', 'C', 'E', 'B', 'D']
```