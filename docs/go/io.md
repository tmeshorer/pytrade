# Reader

```yaml
r := strings.NewReader("reader")
buf := make([]byte,4)
n,err := r.Read(buf)
```

## Copy
```yaml
io.Copy(dst Writer,src Reader)

io.Copy(os.Stdout,r)
```

## Files
```yaml
import "path/filepath"


filepath.Join("dir1","dir2")
fmt.Println(path)
filepath.IsAbs(path)
```

### File info
info = os.Stat("dir)
info.Name()
info.Size()

## Read the file
```yaml
os.ReadFile(path)
```

## Read the file in parh
file,err:= os.Open(path)
for {
    data,err := f.Read(b)
    for {
        n,err := file.Read(b)
    }
}
defer file.Close()

```

# Logging
- Log to spot bugs