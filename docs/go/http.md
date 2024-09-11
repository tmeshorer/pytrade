# HTTP Server
```yaml
func hello(w http.ResponseWriter, req *http.Request) {

}

func main() {
  http.HandleFunc("/hello",hello)
  http.HandleFunc("/headers",headers)
}
```

## Start a server
```yaml
http.ListenAndServe(":8080",nil)
```