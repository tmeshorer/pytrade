## Go routine


```yaml
start := time.Now()
elapsed := time.Since(start)
```
- main function should wait for the go routine. add sleep in the main function

# Main go rountine
- main() function is the main go routine.
- when main() exist, all go rountines exit.
- all go-routine running one near eachother.

# Anonymous go routines
```yaml
go func() {
  
}()
```

# Go routines
- Lightweight application thread. 
- N:M scheduling,
- Each OS thread have one queue - LRQ - Local run queue.
- Go Scheduler - GRQ - global run queue, all go routines that has not been moved.
- Cooperative scheduler - No time based preemption - OS never interrupt a running process.
- When a go routine make function call, there might a context switch. 
- Function call, gc, network calls, channel operation.
- Go routine multiplexed to fewer number of OS threads.
- context switching time is much faster.
- Channels by design 

# WaitGroup 

- main go routine terminate 
- Wait group allow multiple go-routine to wait for each other.
- Syntax

```yaml
var wg sync.WaitGroup
wg.Add(int) // how much gor to wait
wg.Wait()
wg.Done() // decrease 
```


## Select Statement
- look like a switch but for channel
- Wait on multiple communication operations
- Blocks only untill any of the case statement are ready
- If multiple are ready select one at random.
- Let go routine wait on multiple comm operation.
- Powerfull tool for managing sync and concurrency.

```yaml
select {
  ch1
  ch2
  ch3
}
```

```yaml
    c1 := make(chan string)
    c2 := make(chan string)
    go func() {
      time.Sleep(1 * time.Seconds)
      c1 <- "one"
    }()
    select {
      case msg1 := <- c1:
        fmt.Println("recieved,msg1)
    }
```