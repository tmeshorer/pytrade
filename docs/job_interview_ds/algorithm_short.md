## ADT
#### List (ADT)
- Retrieve item at position i
- Insert item as position i
- Delete item as position i
- Length()
- List correspond to loops, matrix corrspons to inner-outer loop.
#### Stack - List implement only
- Insert-Last(L),Ret-Last(L). Del-Last(L)
- List with push/pop LIFO
#### Qeueue - implement only
- Insert-Last(L), Ret-First(L),Del-First(L)
- List with FIFO.
#### Implement List
- Using Array
- Using Circual Array
- Using Single Link List
### Dict ADT
- Insert(I)
- Delete(I)
- Min(D) min key in D
- Max(S) max key in D
#### BST
- Implement Dict
- All operations are log N. 
#### Hash table
- Hash function
- Chaining. 
### Priority Q ADT
- Implement via Heap.
### Graph ADT




# Array
## For interview
- Are there duplicates
- Iteration
- Tech
  - Sliding windows.
  - Two pointers.
  - Traversing from the right.
  - Precomputation
  - Index as hash key
# String
## For interview
- Tech
  - Counting charts - use hashtable
  - Anagram - sort chars/ have the same freq
  - Polyndrom
# Hashtable
## For interview
- Dict
# Recursion
## For interview
- Base case / recursive case
- Break the problem to smaller problem and recurse.
- Know how to generate permutation.
# Sorting and searching
- Quick sort / Merge sort
- Tech
  - Binary Search
# Matrix data type
## Tech
- Create an empty N * M matrix
```python
zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
```
# Linked list data type
- Each element contain the address of the next element. 
- Types:
  - Single linked list : each node point to the next
  - Double linked list: Each node has next and prev pointer.
  - Circular linked list - single linked list where last node point to the head.
- Techs
  - Dummy node
  - Two pointers 
    - K from the last node
    - Detecting cycle
    - Get middle node.

# Queue
Linear collection of elements, addition as one end of the seq `enqueue` and removal from other end
`dequeue`. 

# Stack
Support `push` and `pop`. 

# Interval
### Issue11
```python
def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]
```
```python
def merge_overlapping_intervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]
```

# Tree
- Usually binary tree
- Traversal (in order/pre order/post order)
- Tech
  - Use recursion
  - Traverse by level
  - Summation of nodes.
# Graph
- DFS
- BFS
- Topolgical sort

# Heap
- Max Heap
- Min Heap
- Mention of K
