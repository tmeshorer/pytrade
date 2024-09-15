public class Hello {
    public static void main(String[] args) {
    }
}

## Data types
- int
- double
- boolean
- char
- String

# Decleration in java
```yaml
int a = 0;
int b = 99;
c && b
```

# printing
```yaml
System.out.println("Test")
```
# Parsing
```yaml
Integer.parseInt("23")
Double.parseDouble("22")
```

# Control
## If statement
if (x > y) {

}
## Loop
for (int i= 0;i<10;i++) {
}
## Break
for (int i=0;i<10;i++) {
    if (i % 10 == 0) break
}
## Switch
switch(day) {
    
}

## Array
```yaml
String[] SUITS = {"A","B","C"}
double [] = new double[10]
```
## To dimentioal array
double [][] a = {}

## Function
```yaml
public static double test(int n) {

}
```
# Using an object
String s;
s = new String("test") // ctor

## Instance var
public class Charge {
    double x,y
}
# Collection framework
- ArrayList
- LinkedList implemenet List
- PriorityQueue implements Queue
- HashSet implement Set
- Map - HashMap

## Add / Remove / Check existing
- add
- addAll
- remove
- var list = new GenericList<String>()

## Iterator on a collection
```yaml
Collection<String> collection = new ArrayList<String>()
List.remove(0)
var names = new HashSet<String>()
```