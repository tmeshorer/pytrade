```yaml
 p("Contains:  ", s.Contains("test", "es"))
    p("Count:     ", s.Count("test", "t"))
    p("HasPrefix: ", s.HasPrefix("test", "te"))
    p("HasSuffix: ", s.HasSuffix("test", "st"))
    p("Index:     ", s.Index("test", "e"))
    p("Join:      ", s.Join([]string{"a", "b"}, "-"))
    p("Repeat:    ", s.Repeat("a", 5))
    p("Replace:   ", s.Replace("foo", "o", "0", -1))
    p("Replace:   ", s.Replace("foo", "o", "0", 1))
    p("Split:     ", s.Split("a-b-c-d-e", "-"))
    p("ToLower:   ", s.ToLower("TEST"))
    p("ToUpper:   ", s.ToUpper("test"))
```

## regext
```yaml
    match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
    fmt.Println(match)
```

# Json
```yaml
type response1 struct {
    Page   int
    Fruits []string
}

res1B, _ := json.Marshal(res1D)
fmt.Println(string(res1B))

res := response2{}
json.Unmarshal([]byte(str), &res)
```

# Time
```yaml
now := time.Now()
now.UnixMilli()
now.Year()
now.Month()
diff = now.Sub(then)
```
# Random
```yaml
rand.IntN(100)
```

# Files
```yaml
dat,err := os.ReadFile("/tmp/dat")
fmt.Print(string(dat))
// read bytes
f,err := os.Open("temp/dat")
b1 := make([]byte,5)
n1,err := f.Read(b1)
```
# Directory
```yaml
err := os.Mkdir("subdir",0755)
defer os.RemoveAll("subdir)
os.MkdirAll("a/b/c",0755)
```

# Create Temp File
```yaml
f,err := os.CreateTemp("","sample")
defer os.Remove(f.Name())
```

# Env var
```yaml
os.GetEnv("FOO")
```
# Run process
```yaml
dataCmd := exec.Command("date")
dateOut,err :- dateCmd.Output()
if err := nil {
  panic(err)
}
```

# Exit
```yaml
os.Exit(3)
```