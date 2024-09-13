# Go routine
- Lightweight thread managed by the cluster.
```yaml
go (x,y,z)
```
## Channel type piped
```yaml
ch <- v // send
v := <- ch // recieve
```
## Closed
```yaml
v,ok <-ch
```

in the receiever.
```yaml
for i in range c {
}
```
- only the receiever close the channel.

## Select
The select blocks on multipl operations

```yaml
func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}
```