## String
- equals method
- chatAt(n)
- toUpperCase()
- toLowerCase()
- length()

# Class
```yaml
public class Account {
  private String name;
  private int balance;
  
  public int getBalance() {
    return balance
  }
  
}
```

# Inheritance
```yaml
class CheckingAccount extends Account {
  CheckingAccount(String name) {
    super(name);
  }
  
  @Override
  public String getName() {
  
  }
  
}
```



# List ADT
```yaml
ArrayList<T> = new ArrayList()
```

# Stack ADT
```yam
Stack<String> s= new Stack<String>();
s.push("test")
s.pop()
s.peek()
```


# Queue Adt
```yaml
Queue<String>
add(E e)
offer(E e)
peek()
poll()
```
# Priority Queue ADT
```yaml
Queue<String> pq = new PriorityQueue<String>()
pq.add()
pq.poll()
```

# Map
```yaml
bool containsKey( K key)
bool containsValue( V value)
V get(K k)
put(K key, V value)
remove(K k)
```

# Tree ADT
- One node root
- Traversal
  - Preorder
  - Inorder
  - Postorder

# Set ADT
- collection of members
- TreeSet or HashSet
```yaml
add (E e)
contains(Object)
isEmpty() bool
removeAll(Collection c)
retainAll(Collection c) // intersect
```