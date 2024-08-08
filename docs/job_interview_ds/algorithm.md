# Interview.io 

## Array

### Array
- Fixed memory size
- Multi dimensional array - arr[1][3]
- Use in interview: sorting, searching, dynamic programming
- Iteration:
```python
def square_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]
    return arr
```
- Sort
```python
def sort_elements(arr):
    arr.sort()
    return arr
```
- Searching (Binary search)
```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1
```

- Two pointers - move same direction, oppsitie direction. For string convert to a list first.
```python
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr
```

- Sliding windows

```python
def max_sum_subarray(arr, k):
    # Compute sum of the first window of size k
    # arr[:k] slices the array from index 0 to k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Compute sum of next window of size k by
        # removing the first element of the previous
        # window and adding the next element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Common Array Errors0
- One off

## Linked List

### What is it
ds of set of nodes, each node point to the next node. 




## Hash table

### What is it
key-value data structure.
### Primary use
- When need to remember computation
- Frequencey count
  - Top K freq element
  - Find all anagram in a string
  - Find uniqe char in a string
### DS Python
- Default dict
    
```python
from collections import defaultdict
words = "i love love love interviewing.io"

# initialize every key with a default integer of 0
dictionary = defaultdict(int)
for word in words.split():
  dictionary[word] += 1
print(dictionary) # {i': 1, 'love: 3, 'interviewing.io: 1}
```

### Data tracking and organization
- 