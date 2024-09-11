```yaml
func add(x,y int) int {
   return x+x 
}

func Test_add(t *testing.T) {
  result := add(1,3)
  t.Error("exepcted 5 got",result)

```

- Test files should be named foo_test.go

## Table tests
data := [] struct {
    name string
    num1 int
    num2 int
    op   string
    expected int
}

- t.Parallel() allow running test cuncurrently.
- go test -v -cover.

