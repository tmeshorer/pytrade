# Variables
- declare 1 or more
- declare a var with zero value
```yaml
var e int
```
# Constants
- like var
- const create a constant value
```yaml
const s string = "test"
const n = 1000
```
# For loop
- go only looping construct.
```yaml
for j:=0;j<3;j++ {
  fmt.Println(j)
}
```
- range over an integer
```yaml
for j := range 3 {
}
```
# Switch
switch i {
    case 1:
      fmt.Println(1)
    case 2:
      fmt.Println(2)
}

# Slice
```yaml
var s []string

s = make([]string,3)
```
- len(s) return the legnth of the slice
```yaml
len(s)
```
## Add to slice
```yaml
s = append(s,"d")
```

## Slice 
```yaml
l = s[2:5]
l = s[:5]
```

## Slices Package
```yaml
slices.Equal(t,t2)
slices.Sort(t)
```

## 2 dim slice
```yaml
twoD := make([][]int,3)
for i := range 3 {
  innerLen := i+1
  
}
```

# Map
Associatave data type
- if the key does not exist zero value returned.
- 
```yaml
 m:= make(map[string]int)
 m["1"] = 1
 v:= m["1]
 delete(m,"k2") // delete c key
 clear(m) // clear the map
```
## Check if a key is in a map
    _,prs := m["k2"]

# Function
## require explicit return
```yaml
func plus(a int, b int) int {
  return a+b
}
```

## Multiple return values
```yaml

func vals() (int,int) {
  return 3,7
}
```
## Vardic function
- can be called with any number of arguments
```yaml
func sum(num...int) {
  for _,v:=range num {
    total+=sum
  }
  return total
}
```
## Clouseres
- Anonum functions
```yaml
func intSeq() func() int {
  i := 0
  return func() int {
    i++
    return i
  }
}
```
## Recursion
```yaml
func fact(n int) int {
  if n == 0 {
    return 1
  }
  return n*fact(n-1)
}
```

# Range over build in type
- range over a number
- range over a slice
- range over a map
- range over a map keys

# Pointers
- Allow to pass reference to values
```yaml
func zeroptr(iptr *int) {
  *iptr = 0
}
  
i:=1  
zeroptr(i)

fmt.Println("pointer", &i)
```

# String
- Readonly slice of bytes.
- Text encoded in utf8
```yaml
 const s := "test"
 len(s)
 s[1]
``` 

# Struct
- collection of fileds, form a record
- new initilize a struct
- access fields with .
- 
```yaml
type person struct {
  name string
  age int
}

func New(name string) &person {
  return &person {name:name}
}
```
## Method
```yaml
func (r *person) Name() string {
    return r.Name
}
```

- Value reciever
```yaml
func (r *person) Name() string {
    return r.Name
}
```

# Interfaces
- Collection of vector signatures
- To implement the interface, we must implement the methods
```yaml
type goem interface{
  area() float64
  perim() float64
}

func measure(g goem) {
}
```

## Enum
type ServerState int

const (
    StateIdle = iota
    StateConnected
    StateError
    StateRetry
)

# Struct Embedding

# Generic
- Type parameters

# Errors
```yaml
fmt.Erorrf
```

# Custom Error
```yaml
type argError struct {
    arg     int
    message string
}
Adding this Error method makes argError implement the error interface.

func (e *argError) Error() string {
    return fmt.Sprintf("%d - %s", e.arg, e.message)
}
```

# Go routine
Lightweight thread of execution
```yaml
go f("test")
```
- annonymous functions
```yaml
go func(msg string) {
  fmt.Println("test")
}("going")
```

# Channel
Channels are the pipe to connect current 

```yaml
    message := make(chan string)
    go func() { messages <- "ping" }
    msg :<- messages
```

# Channel sync
```yaml
done := make(chan book,1)
go worker(done)

func worker(done chan bool) {
  fmt.Print("staff")
  done <- chan
}
```

# Select
- wait on multiple channels

```yaml
select {
    case msg1 := <-c1:
        fmt.Println("received", msg1)
    case msg2 := <-c2:
        fmt.Println("received", msg2)
    }
```

# Timeout

```yaml
// For our example, suppose we're executing an external
	// call that returns its result on a channel `c1`
	// after 2s. Note that the channel is buffered, so the
	// send in the goroutine is nonblocking. This is a
	// common pattern to prevent goroutine leaks in case the
	// channel is never read.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// Here's the `select` implementing a timeout.
	// `res := <-c1` awaits the result and `<-time.After`
	// awaits a value to be sent after the timeout of
	// 1s. Since `select` proceeds with the first
	// receive that's ready, we'll take the timeout case
	// if the operation takes more than the allowed 1s.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}
```

# Close channel




# Timer
```yaml
// Timers represent a single event in the future. You
	// tell the timer how long you want to wait, and it
	// provides a channel that will be notified at that
	// time. This timer will wait 2 seconds.
	timer1 := time.NewTimer(2 * time.Second)

	// The `<-timer1.C` blocks on the timer's channel `C`
	// until it sends a value indicating that the timer
	// fired.
	<-timer1.C
```

# WaitGroup
Wait for multiple go rutine to finish
```yaml
// This WaitGroup is used to wait for all the
	// goroutines launched here to finish. Note: if a WaitGroup is
	// explicitly passed into functions, it should be done *by pointer*.
	var wg sync.WaitGroup

	// Launch several goroutines and increment the WaitGroup
	// counter for each.
	for i := 1; i <= 5; i++ {
		wg.Add(1)

		// Wrap the worker call in a closure that makes sure to tell
		// the WaitGroup that this worker is done. This way the worker
		// itself does not have to be aware of the concurrency primitives
		// involved in its execution.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Block until the WaitGroup counter goes back to 0;
	// all the workers notified they're done.
	wg.Wait()

```

# Mutex
Mutex protect access to struct

```yaml
type Container struct {
    mu       sync.Mutex
    counters map[string]int
}

func (c *Container) inc(name string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.counters[name]++
}
```

# Statefull gorountin
Another option is to use the built-in synchronization features of goroutines and channels to achieve the same result. This channel-based approach aligns with Go’s ideas of sharing memory by communicating and having each piece of data owned by exactly 1 goroutine.

```yaml
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// As before we'll count how many operations we perform.
	var readOps uint64
	var writeOps uint64

	// The `reads` and `writes` channels will be used by
	// other goroutines to issue read and write requests,
	// respectively.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// Here is the goroutine that owns the `state`, which
	// is a map as in the previous example but now private
	// to the stateful goroutine. This goroutine repeatedly
	// selects on the `reads` and `writes` channels,
	// responding to requests as they arrive. A response
	// is executed by first performing the requested
	// operation and then sending a value on the response
	// channel `resp` to indicate success (and the desired
	// value in the case of `reads`).
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// This starts 100 goroutines to issue reads to the
	// state-owning goroutine via the `reads` channel.
	// Each read requires constructing a `readOp`, sending
	// it over the `reads` channel, and then receiving the
	// result over the provided `resp` channel.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

```

# Sorting
```yaml
 ints := []int{7, 2, 4}
 slices.Sort(ints)
```

# Sorting by function
```yaml
type Person struct {
		name string
		age  int
	}

	people := []Person{
		Person{name: "Jax", age: 37},
		Person{name: "TJ", age: 25},
		Person{name: "Alex", age: 72},
	}

	// Sort `people` by age using `slices.SortFunc`.
	//
	// Note: if the `Person` struct is large,
	// you may want the slice to contain `*Person` instead
	// and adjust the sorting function accordingly. If in
	// doubt, [benchmark](testing-and-benchmarking)!
	slices.SortFunc(people,
		func(a, b Person) int {
			return cmp.Compare(a.age, b.age)
		})
```

# Panic
Panic occur if something wend wrong.
```yaml
if err != nil {
  panic(err)
}
```

# Defer
Ensure that the program defer function call
```yaml
 f := createFile("/tmp/defer.txt")
    defer closeFile(f)
    writeFile(f
```

# Recover
```yaml

Go makes it possible to recover from a panic, 
by using the recover built-in function. 
A recover can stop a panic from aborting the program and 
let it continue with execution instead.

defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered. Error:\n", r)
        }
    }()
```

# Errors functions 