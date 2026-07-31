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
Bubble Sort repeatedly compares adjacent elements and swaps them if they're in wrong order, gradually moving larger elements to the end like bubbles rising in water.

**Step-by-Step:**
1. Start at the beginning, compare each pair of neighbors
2. Swap if the left one is bigger than the right one
3. Keep doing this for the whole array, but shorten the range each time since the end gets sorted
4. Stop early if you go through a whole pass without any swaps - means it's already sorted

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
Selection Sort finds the smallest element in the unsorted part and swaps it with the first unsorted element, gradually building a sorted portion at the beginning.

**Step-by-Step:**
1. Look at the whole array - nothing's sorted yet
2. Find the smallest element in the entire array
3. Swap it with the first element - now the first position is sorted
4. Now ignore the first element and find the smallest in the remaining part
5. Swap that with the second position, and so on
6. Keep doing this until you've placed everything in order

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
Insertion Sort builds the sorted array one element at a time by taking each element and inserting it into its correct position in the already sorted part, like sorting playing cards.

**Step-by-Step:**
1. Start with just the first element - that's already "sorted"
2. Take the next element and compare it with the sorted part
3. Shift all bigger elements in the sorted part one position to the right
4. Insert the current element in its correct spot
5. Now the first two elements are sorted, repeat for the third, and so on
6. Keep expanding the sorted portion until the whole array is done

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
Merge Sort divides the array into halves recursively until you have single elements, then merges them back together in sorted order, guaranteeing O(n log n) performance.

**Step-by-Step:**
1. Split the array right down the middle into two halves
2. Keep splitting each half until you have arrays of one element each
3. Now start merging: take two sorted arrays and combine them
4. Compare elements from both arrays, pick the smaller one first
5. Keep doing this until one array is empty, then add the rest
6. Work your way back up, merging larger and larger sorted chunks

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
Quick Sort picks a pivot element, partitions the array so smaller elements go left and larger go right, then recursively sorts the two partitions.

**Step-by-Step:**
1. Choose a pivot - usually the last element, but could be anything
2. Partition the array: put everything smaller than pivot on the left, larger on the right
3. The pivot is now in its final position
4. Recursively apply the same process to the left partition
5. And to the right partition
6. Keep going until you have single elements or empty arrays

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
Heap Sort builds a max-heap from the array, then repeatedly extracts the largest element (root) and places it at the end, rebuilding the heap each time.

**Step-by-Step:**
1. Turn the entire array into a max-heap (where parent is always bigger than children)
2. Swap the root (largest element) with the last element in the heap
3. Reduce the heap size by 1 (the swapped element is now sorted at the end)
4. Fix the heap property by heapifying the new root down
5. Repeat: extract max, place at end, heapify, until heap is size 1

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
Counting Sort counts how many times each value appears, then uses those counts to place elements in their correct positions in the output array.

**Step-by-Step:**
1. Find the range of values (min to max) in your array
2. Create a count array that's big enough to hold counts for each possible value
3. Go through the input array and count how many times each value appears
4. Modify the count array so each position shows how many elements are <= that value
5. Create an output array and place each element in its sorted position using the counts
6. Copy everything back to the original array

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
Radix Sort sorts numbers by processing one digit at a time, starting from the rightmost digit, using a stable sort like counting sort for each digit position.

**Step-by-Step:**
1. Find the largest number to know how many digits you need to process
2. Start with the rightmost digit (units place)
3. Sort the entire array based only on that digit using counting sort
4. Move to the next digit (tens place) and sort again based on that digit
5. Keep going left through all digits - hundreds, thousands, etc.
6. After sorting by the leftmost digit, you're done

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
Bucket Sort distributes elements into several buckets based on their values, sorts each bucket individually, then concatenates them for the final sorted result.

**Step-by-Step:**
1. Decide how many buckets you want based on the data range
2. Create empty buckets (like containers)
3. For each element, figure out which bucket it belongs in based on its value
4. Drop each element into its appropriate bucket
5. Sort each bucket using any sorting method (insertion sort works well for small buckets)
6. Go through the buckets in order and collect all the sorted elements

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
