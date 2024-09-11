# Go routine basic
- Start a go routine
```yaml
go f()
```
- Send a valud
```yaml
ch <- value
```
- Recieve a value
```yaml
value = <- ch
```

- Worker task
```yaml
func worker(in <-chan *Work, out chan <- *Work) {
 for w := range in {
    w.z = w.x * w.y
    out <- w
 }
}
```

- service pattern
```yaml
func (s *Service) Start() chan request {
 ch := make(chan request)
 go s.serve(ch) // s.serve runs concurrently
 return ch // returns immediately
 }
```
