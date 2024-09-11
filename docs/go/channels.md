#
- Channel are a mean which differnt go-routines communicate
- Share memory by communicating.
- Shared DS are proceted by Mutex. 
- Use of channels to pass memory, share memory by communicating
- Bi direction
- channel hold data of one data type

```yaml
var c chan string
c:= make (chan string)
```
- sending a value, receiving a value

# Send a value
```yaml
ch <- v // assignable to the type of the channel
```

# recieved a value
v:= <- ch

# close the channel
```yaml
close(ch)
```

# Query the buffer
```yaml
len(ch)
```

# in a function
```yaml
func sell(ch chan string) {
  ch <- "Furniture"
  fmt.Println("Send)
}

func buy(ch chan string) {
  val := <-ch
}

func main() {
  ch := make(chan string)
  go buy(ch)
  go sell(ch)
}
```

# Unbuffered channel



# Closing the channel
```yaml
c,ok := <- ch
close(ch)  
if !ok { // channel close
}
```

## Range on channel
```yaml
func buy(ch chan int, wg *sync.WaitGroup) {
  for val := range ch {
    fmt.Println("recv",val)
  }
  wg.Done()
}
```