# Data Structures: Trees and Graphs

This document covers fundamental data structures including Trees, Graphs, Binary Trees, Binary Search Trees, and traversal algorithms BFS and DFS. Each section includes detailed explanations, time and space complexities, working principles, and basic JavaScript implementations.

## Table of Contents

- [Trees and Graphs](#trees-and-graphs)
- [Binary Tree and Binary Search Tree](#binary-tree-and-binary-search-tree)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)

## Trees and Graphs

### Trees

Trees are hierarchical structures where you have a root node at the top, and each node can have multiple children, but no cycles - it's like a family tree or a company org chart.

### Graphs

Graphs are more flexible - just nodes connected by edges. They can have cycles, be directed (one-way streets) or undirected (two-way), and edges can have weights (like distances) or not.

### Time Complexity
- **Tree Operations**: Depends on what you're doing - could be O(1) for some things, O(n) for others
- **Graph Operations**: Varies by how you store it and what operation

### Space Complexity
- **Adjacency Matrix**: O(V²) - like a big table showing connections between every pair
- **Adjacency List**: O(V + E) - each node just lists its friends

### How They Work
Trees are perfect for hierarchical stuff like file systems or org charts. Graphs handle relationships like social networks, maps, or web pages where connections can be complex.

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

A binary tree is just a tree where each node has at most two children - left and right. That's it! No other restrictions.

### Binary Search Tree (BST)

Now BST adds rules: left child must be smaller than parent, right child must be bigger. Both subtrees follow the same rule. This gives you sorted order automatically.

### Time Complexity
- **Binary Tree Operations**: Search/insert/delete can be O(n) in worst case, O(log n) if balanced
- **BST Operations**: Same as above - depends on height. Balanced = O(log n), skewed = O(n)

### Space Complexity
- O(n) - just storing the nodes

### How They Work

Binary trees are the foundation. BSTs are special because they maintain sorted order, so searching is fast when balanced. But if it gets skewed (like a linked list), performance tanks.

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

BFS explores a graph level by level - like checking all your immediate friends first, then their friends, and so on. Uses a queue to keep track of what to visit next.

### Time Complexity
- O(V + E) - you visit each node and edge exactly once

### Space Complexity
- O(V) worst case - the queue could hold all nodes if it's a dense graph

### How It Works
Start at one node, visit all its direct neighbors first, then go to the next level. Perfect for finding shortest paths in unweighted graphs or doing level-order traversal in trees.

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

DFS goes as deep as possible down one path before backtracking - like exploring a maze by always going left until you hit a dead end, then backtracking. Uses a stack (or recursion).

### Time Complexity
- O(V + E) - visits each node and edge once

### Space Complexity
- O(V) worst case for the recursion stack, or O(h) where h is the deepest path

### How It Works
Start at one node, keep following one neighbor as far as you can, then backtrack when you can't go further. Great for topological sorting, cycle detection, and maze solving.

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