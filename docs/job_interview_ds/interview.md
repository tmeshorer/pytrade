# General

## Skills
1) The ability to formulate real world problems
2) The skills to solve problems and design algorithms
3) The tools to go from algorithms to a tested program

## During interview
1) Work on small example
2) Think outload
3) Spell out brute force solution
4) Test corner case
5) Use proper syntax



# Links
  - (python leetcode) https://www.linkedin.com/feed/update/urn:li:activity:7030707694445490176?utm_source=share&utm_medium=member_desktop
  - what we look for in resume: https://huyenchip.com/2023/01/24/what-we-look-for-in-a-candidate.html
# Data structure

## Linked List
```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

### Iteration
```python
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
```
### Insertion Single
```python

```
### Insertion Double
### Deletion Single
### Deletion Double
### Reverse a linked list
```python
def reverse(self):
    prev = None 
    cur  = self.head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    self.head = prev
``` 
## Binary Tree
```python
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None
```

```python
class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
```


### Size
```python
    def size(self,node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
```
### Height
```python
    def height(self,node):
        if node == None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1+max(left_h,right_h)
```
### Traversal
#### Preorder
```python
    def preorder(self,)
```

## Binary Search Tree
### Insertion
    ```python
        def insert (self,new_val):
            self.insert_helper(self.root,new_val)

        def insert_helper(self,current,new_val):
            if current.data < new_val:
                if current.right:
                    self.insert_helper(current.right,new_val)
                else:
                    current.right = Node(new_val)
            else:
                if current.left:
                    self.insert_helper(current.left,new_val)
                else:
                    current.left = Node(new_val)
    ```
### Search
```python
      def search(self,value):
        self.search_helper(self,self.root,value)

      def search_helper(self,node,value):
          if node == None:
                return False
          if node.value == value:
             return True
          if node.value < value:
              return self.search_helper(node.right,value)
          else:
              return self.search_helper(node.left,value)
          
        
```    
### Max
### See if tree is balanced


## Tries
## Stack
## Heap
- Find the largest M items in a stream of N Items

### Min heap
### Max heap
## Q
## Vector/List
### Longest Polyndrome substring
### Maze traversal in 2D matrix
## Hashtable
# Graph
  - Node : Vertex
  - Connection : Edge
  ```python
    n = 5
    graph = [[] for _ in range(n)]
    graph[0] = [1,2]
    graph[1] = [3]
  ``` 

# Algorithms

## BFS
## DFS
    def dfs(v,visited,graph):
        if not visited[v]:
            visited[v] = True
            for w in graph[v]:
                dfs(w,visited,graph)
    
    
## Backtracking
## Binary Search
```python
def bin_search(data,target,low,high):
    if low>high:
        return False
    mid = (low+high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return bin_search(data,target,low,mid-1)
    else:
        return bin_search(data,target,mid+1,high)
```

## Merge sort
## Quick sort
## Tree insert / find
   - Pre order - visit the root first, left , right
   - Inorder - visit left, root , right
   - Post order - left , right , root. 
# Concepts
## Recursion
  - Base case - check if the current problem is a simple case
  - Recurse - divide the problem and recurse.
  - It must be possible to decompose the original problem.
