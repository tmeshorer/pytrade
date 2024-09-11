# Create new error

```yaml
err := errors.New("Custom error occured")
```

# print error

```yaml
fmt.Errorf("in filechecker: %w",err)
```

# Checking is

```yaml
 if errors.Is(err, os.ErrNotExist) {
            fmt.Println("That file doesn't exist")
        }
```
