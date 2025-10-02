# Sorting Algorithms

This document covers various sorting algorithms, including their time and space complexities, step-by-step approaches, and optimized JavaScript implementations.

## Table of Contents

- [Bubble Sort](#bubble-sort)
- [Selection Sort](#selection-sort)
- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)
- [Quick Sort](#quick-sort)
- [Heap Sort](#heap-sort)
- [Counting Sort](#counting-sort)
- [Radix Sort](#radix-sort)
- [Bucket Sort](#bucket-sort)

## Bubble Sort

### Time Complexity
- **Best Case**: O(n) - When the array is already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - When the array is reverse sorted

### Space Complexity
- O(1) - In-place sorting

### Approach
1. Start from the beginning of the array.
2. Compare each pair of adjacent elements.
3. If the current element is greater than the next, swap them.
4. Continue this process for each element in the array.
5. After each pass, the largest element bubbles to the end.
6. Repeat the process for n-1 passes, where n is the array length.
7. Optimization: If no swaps occur in a pass, the array is sorted.

### JavaScript Implementation
```javascript
function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    for (let i = 0; i < n - 1; i++) {
        swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}
```

## Selection Sort

### Time Complexity
- **Best Case**: O(n²)
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

### Space Complexity
- O(1) - In-place sorting

### Approach
1. Divide the array into sorted and unsorted parts.
2. Initially, the sorted part is empty, unsorted is the whole array.
3. Find the minimum element in the unsorted part.
4. Swap it with the first element of the unsorted part.
5. Move the boundary between sorted and unsorted parts one element to the right.
6. Repeat until the entire array is sorted.

### JavaScript Implementation
```javascript
function selectionSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex !== i) {
            [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
        }
    }
    return arr;
}
```

## Insertion Sort

### Time Complexity
- **Best Case**: O(n) - When the array is already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - When the array is reverse sorted

### Space Complexity
- O(1) - In-place sorting

### Approach
1. Start with the second element (index 1).
2. Compare it with the previous elements.
3. Shift all larger elements to the right to make space.
4. Insert the current element in its correct position.
5. Repeat for each subsequent element.

### JavaScript Implementation
```javascript
function insertionSort(arr) {
    let n = arr.length;
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}
```

## Merge Sort

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
- O(n) - Due to the auxiliary array used for merging

### Approach
1. Divide the array into two halves recursively until each subarray has one element.
2. Merge the sorted subarrays:
   - Compare elements from both subarrays.
   - Place the smaller element into the merged array.
   - Continue until one subarray is exhausted.
   - Copy remaining elements from the other subarray.
3. Repeat the merge process up the recursion tree.

### JavaScript Implementation
```javascript
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    
    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    
    return merge(left, right);
}

function merge(left, right) {
    let result = [];
    let i = 0, j = 0;
    
    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            result.push(left[i++]);
        } else {
            result.push(right[j++]);
        }
    }
    
    return result.concat(left.slice(i)).concat(right.slice(j));
}
```

## Quick Sort

### Time Complexity
- **Best Case**: O(n log n) - When pivot divides array evenly
- **Average Case**: O(n log n)
- **Worst Case**: O(n²) - When pivot is always the smallest or largest element

### Space Complexity
- O(log n) - Due to recursion stack

### Approach
1. Choose a pivot element from the array.
2. Partition the array around the pivot:
   - Elements smaller than pivot go to the left.
   - Elements larger than pivot go to the right.
3. Recursively apply quicksort to the left and right subarrays.
4. The array is sorted when all subarrays are sorted.

### JavaScript Implementation
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

## Heap Sort

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
- O(1) - In-place sorting (excluding the space for the heap)

### Approach
1. Build a max-heap from the array.
2. Swap the root (maximum element) with the last element.
3. Reduce the heap size by 1 and heapify the root.
4. Repeat until the heap size is 1.

### JavaScript Implementation
```javascript
function heapSort(arr) {
    const n = arr.length;
    
    // Build max heap
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // Extract elements from heap
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
    
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
}
```

## Counting Sort

### Time Complexity
- **Best Case**: O(n + k)
- **Average Case**: O(n + k)
- **Worst Case**: O(n + k)
- Where k is the range of input values

### Space Complexity
- O(n + k) - For count array and output array

### Approach
1. Find the maximum value in the array to determine the range.
2. Create a count array of size max+1, initialized to 0.
3. Count the occurrences of each element in the input array.
4. Modify the count array to store cumulative counts.
5. Create an output array and place elements in sorted order using the count array.
6. Copy the output array back to the original array.

### JavaScript Implementation
```javascript
function countingSort(arr) {
    if (arr.length <= 1) return arr;
    
    const max = Math.max(...arr);
    const min = Math.min(...arr);
    const range = max - min + 1;
    const count = new Array(range).fill(0);
    const output = new Array(arr.length);
    
    // Count occurrences
    for (let i = 0; i < arr.length; i++) {
        count[arr[i] - min]++;
    }
    
    // Cumulative count
    for (let i = 1; i < count.length; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    for (let i = arr.length - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }
    
    // Copy back to original array
    for (let i = 0; i < arr.length; i++) {
        arr[i] = output[i];
    }
    
    return arr;
}
```

## Radix Sort

### Time Complexity
- **Best Case**: O(n * d)
- **Average Case**: O(n * d)
- **Worst Case**: O(n * d)
- Where d is the number of digits in the maximum number

### Space Complexity
- O(n + k) - For count array and output array

### Approach
1. Find the maximum number to determine the number of digits.
2. Perform counting sort for each digit, starting from the least significant digit.
3. Use a stable sort (counting sort) to maintain relative order.
4. Repeat for each digit place until all digits are processed.

### JavaScript Implementation
```javascript
function radixSort(arr) {
    if (arr.length <= 1) return arr;
    
    const max = Math.max(...arr);
    let exp = 1;
    
    while (Math.floor(max / exp) > 0) {
        countingSortByDigit(arr, exp);
        exp *= 10;
    }
    
    return arr;
}

function countingSortByDigit(arr, exp) {
    const n = arr.length;
    const output = new Array(n);
    const count = new Array(10).fill(0);
    
    // Count occurrences of digits
    for (let i = 0; i < n; i++) {
        const digit = Math.floor(arr[i] / exp) % 10;
        count[digit]++;
    }
    
    // Cumulative count
    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    for (let i = n - 1; i >= 0; i--) {
        const digit = Math.floor(arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }
    
    // Copy back to original array
    for (let i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}
```

## Bucket Sort

### Time Complexity
- **Best Case**: O(n + k)
- **Average Case**: O(n + k)
- **Worst Case**: O(n²) - When all elements go to the same bucket

### Space Complexity
- O(n + k) - For buckets and elements

### Approach
1. Create k empty buckets (or lists).
2. Distribute elements into buckets based on a hash function.
3. Sort each bucket individually (using another sorting algorithm).
4. Concatenate all sorted buckets.

### JavaScript Implementation
```javascript
function bucketSort(arr, bucketSize = 5) {
    if (arr.length <= 1) return arr;
    
    const min = Math.min(...arr);
    const max = Math.max(...arr);
    const bucketCount = Math.floor((max - min) / bucketSize) + 1;
    const buckets = Array.from({ length: bucketCount }, () => []);
    
    // Distribute elements into buckets
    for (let i = 0; i < arr.length; i++) {
        const bucketIndex = Math.floor((arr[i] - min) / bucketSize);
        buckets[bucketIndex].push(arr[i]);
    }
    
    // Sort each bucket and concatenate
    const sortedArr = [];
    for (let i = 0; i < buckets.length; i++) {
        if (buckets[i].length > 0) {
            buckets[i].sort((a, b) => a - b);
            sortedArr.push(...buckets[i]);
        }
    }
    
    return sortedArr;
}
```
