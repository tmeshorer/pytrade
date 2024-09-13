- Stream sockets
- UDP Sockets
- Server
  - socket
  - bind <IP:80>
  - listen
  - accept
- Client
  - socket
  - connect() <IP:80>
  - accept - create new socket 
  - read() / write()
- Both call close() 

```yaml
kn, err:= net.Listen("tcp",":8080")

for {
  conn,err := ln.Accept()
  go HandleConn(conn)
}
```

- Handle connection
```yaml
func handleConn(conn net.Conn) {
  for {
    buf = make([]byte,1024)
    side,err = conn.Read(buf)
  
  }
  data = buf[:size]
  conn.Write([]byte())
  }
  

}
```

- UDP
- Server
  - socket()
  - bind()
  - recvfrom()
  - sendto()

pc,err := net.ListenPacket("udp",":8080")