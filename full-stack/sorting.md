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
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the list (beginning) while larger elements sink to the bottom (end). It solves the sorting problem by making multiple passes through the array, gradually moving larger elements towards the end with each pass.

**Detailed Step-by-Step Approach:**
1. Start from the beginning of the array (index 0).
2. Compare the current element with the next adjacent element.
3. If the current element is greater than the next element, swap them.
4. Move to the next pair of adjacent elements and repeat the comparison and swap if needed.
5. Continue this process until you reach the end of the unsorted portion of the array.
6. After each complete pass, the largest unsorted element will have "bubbled" to its correct position at the end.
7. Repeat the entire process for n-1 passes, where n is the array length, reducing the range of comparison by one each time.
8. **Optimization**: Track if any swaps occurred during a pass. If no swaps happened, the array is already sorted and we can terminate early.

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
Selection Sort is an in-place comparison sorting algorithm that divides the input list into two parts: a sorted sublist at the beginning and an unsorted sublist at the end. It solves the sorting problem by repeatedly finding the minimum element from the unsorted portion and moving it to the end of the sorted portion. This algorithm is called "selection" sort because it repeatedly selects the smallest (or largest) element from the unsorted portion and places it at the beginning of the sorted portion.

**Detailed Step-by-Step Approach:**
1. Divide the array into two parts: sorted (initially empty) and unsorted (initially the entire array).
2. Find the minimum element in the unsorted portion of the array.
3. Swap this minimum element with the first element of the unsorted portion (which becomes the last element of the sorted portion).
4. Expand the sorted portion by moving the boundary one position to the right.
5. Repeat steps 2-4 until the entire array is sorted.
6. The algorithm maintains the invariant that all elements before the current position are sorted and smaller than all elements after it.

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
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by taking elements from the unsorted portion and inserting them into their correct position in the sorted portion. The algorithm solves the sorting problem by maintaining a sorted subarray at the beginning, gradually expanding it by inserting each subsequent element into its proper place within the sorted subarray. This is similar to how people sort playing cards in their hands.

**Detailed Step-by-Step Approach:**
1. Start with the second element (index 1) as the first element (index 0) is considered already sorted.
2. Take the current element and compare it with elements in the sorted portion (to its left).
3. Shift all larger elements in the sorted portion one position to the right to make space.
4. Insert the current element into its correct position within the sorted portion.
5. Move to the next element and repeat the process.
6. Continue until all elements have been inserted into their correct positions in the sorted array.
7. The algorithm maintains that at each iteration, the subarray from index 0 to i is sorted.

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
Merge Sort is a divide-and-conquer sorting algorithm that divides the unsorted list into n sublists, each containing one element (a list of one element is considered sorted), then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining. It solves the sorting problem by breaking down the array into smaller, manageable pieces, sorting them individually, and then merging them back together in sorted order. This approach ensures consistent O(n log n) performance regardless of input distribution.

**Detailed Step-by-Step Approach:**
1. **Divide**: If the array has more than one element, split it into two halves of roughly equal size.
2. **Conquer**: Recursively sort both halves using the same merge sort algorithm.
3. **Combine**: Merge the two sorted halves into a single sorted array by:
   - Create a temporary array to hold the merged result.
   - Compare elements from both halves and place the smaller element into the result array.
   - Continue until one half is exhausted, then copy remaining elements from the other half.
4. **Base Case**: When the subarray has 0 or 1 elements, it is already sorted.
5. The recursion continues until the entire array is sorted through successive merges.

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
Quick Sort is a highly efficient divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. It solves the sorting problem by recursively sorting the sub-arrays created by partitioning. The algorithm is called "quick" because it can sort a list much faster than other algorithms in practice, though its worst-case performance can be poor if the pivot selection is suboptimal.

**Detailed Step-by-Step Approach:**
1. **Choose Pivot**: Select a pivot element from the array (commonly the last element, but can be random or median for better performance).
2. **Partition**: Rearrange the array so that:
   - All elements smaller than the pivot are moved to the left of the pivot.
   - All elements greater than the pivot are moved to the right of the pivot.
   - The pivot is now in its final sorted position.
3. **Recurse**: Apply the same quicksort algorithm recursively to the left subarray (elements < pivot) and right subarray (elements > pivot).
4. **Base Case**: When a subarray has 0 or 1 elements, it is already sorted.
5. The recursion continues until all subarrays are sorted, resulting in a fully sorted array.

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
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It solves the sorting problem by first building a max-heap from the input array, then repeatedly extracting the maximum element from the heap and placing it at the end of the sorted array. The algorithm works by treating the array as a complete binary tree and maintaining the heap property where parent nodes are larger than their children. This approach provides consistent O(n log n) performance and is performed in-place.

**Detailed Step-by-Step Approach:**
1. **Build Max-Heap**: Transform the input array into a max-heap by starting from the last non-leaf node and performing heapify operations upwards to the root.
2. **Extract Maximum**: Swap the root (maximum element) with the last element of the heap.
3. **Reduce Heap Size**: Decrease the heap size by 1 (effectively removing the last element, which is now the maximum).
4. **Heapify Root**: Restore the max-heap property by heapifying the new root element down the tree.
5. **Repeat**: Continue steps 2-4 until the heap size is reduced to 1.
6. The algorithm maintains that after each extraction, the remaining elements form a valid max-heap, and the extracted elements are placed in sorted order at the end of the array.

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
Counting Sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each unique element in the input array. It solves the sorting problem by using the count of each element to determine its position in the sorted output array. This algorithm is efficient when the range of input values (k) is not significantly larger than the number of elements (n), making it ideal for sorting integers with a small range. Unlike comparison sorts, it doesn't compare elements directly but uses arithmetic operations on their values.

**Detailed Step-by-Step Approach:**
1. **Find Range**: Determine the minimum and maximum values in the input array to calculate the range of values.
2. **Initialize Count Array**: Create a count array of size (max - min + 1) and initialize all elements to 0.
3. **Count Occurrences**: Iterate through the input array and increment the count for each element's corresponding index in the count array.
4. **Cumulative Sum**: Modify the count array to store cumulative sums, which will give the correct positions of elements in the sorted output.
5. **Build Output Array**: Create a new output array and place each element from the input array into its correct sorted position using the cumulative count array.
6. **Copy Back**: Copy the sorted elements from the output array back to the original input array.
7. The algorithm ensures stability by processing elements in reverse order during the output phase.

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
Radix Sort is a non-comparison integer sorting algorithm that sorts data by grouping individual digits of the same place value. It solves the sorting problem by processing digits from the least significant to the most significant, using a stable sorting algorithm (like counting sort) for each digit place. This approach is efficient for sorting large numbers of integers or strings with fixed-length representations, as it processes one digit at a time rather than comparing entire numbers. The algorithm gets its name from the Latin word "radix" meaning "root" or "base," referring to the base of the number system.

**Detailed Step-by-Step Approach:**
1. **Find Maximum**: Determine the maximum number in the array to know the number of digits to process.
2. **Initialize Exponent**: Start with the least significant digit (units place) by setting exponent to 1 (10^0).
3. **Sort by Digit Place**: For each digit place (units, tens, hundreds, etc.):
   - Use a stable sorting algorithm (counting sort) to sort the array based on the current digit place.
   - Extract the digit at the current place using modulo and integer division operations.
   - Maintain the relative order of elements with the same digit (stability is crucial).
4. **Increment Exponent**: Multiply the exponent by 10 to move to the next digit place.
5. **Repeat**: Continue the process until all digit places have been processed (when exponent exceeds the maximum number).
6. The algorithm ensures that numbers are sorted correctly because more significant digits take precedence over less significant ones.

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
Bucket Sort is a distribution sorting algorithm that works by distributing elements into a number of buckets, sorting each bucket individually, and then concatenating the sorted buckets. It solves the sorting problem by dividing the range of input values into smaller intervals (buckets) and sorting elements within each interval separately. This approach is particularly effective when input elements are uniformly distributed across a range, as it can achieve better than O(n log n) performance in the average case. The algorithm is also known as bin sort and is useful for sorting floating-point numbers or when additional information about the input distribution is available.

**Detailed Step-by-Step Approach:**
1. **Determine Bucket Count**: Calculate the number of buckets needed based on the input range and desired bucket size.
2. **Create Buckets**: Initialize an array of empty buckets (typically linked lists or arrays).
3. **Distribute Elements**: For each element in the input array:
   - Calculate which bucket it belongs to using a hash function (usually based on the element's value relative to the range).
   - Insert the element into the appropriate bucket.
4. **Sort Individual Buckets**: Sort each non-empty bucket using a suitable sorting algorithm (often insertion sort for small buckets).
5. **Concatenate Results**: Combine all sorted buckets in order to produce the final sorted array.
6. The algorithm's efficiency depends on the uniform distribution of elements across buckets - if all elements fall into one bucket, it degrades to the performance of the chosen sorting algorithm for that bucket.

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
