# Basic networking in linux

- A -> B
- eth0 - interface on each host
```commandline
ip link
```
- Add IP 
```commandline
ip addr add 192.168.1.10/24 dev eth0
```

- Computer can communicate with the switch. 
```commandline
ping 192.168.1.11
```

- Another system
- How do they talk - Router
- Router connect two network together. Server with two network port.
- Two IP, one on each network. 
- Router
  - 192.168.1.1
  - 192.168.2.1
## Gateway
```commandline
route
```
```commandline
ip router add 192.168.2.0/24 via 192.168.0.1.
```
- default gateway to the internet
```commandline
ip route add default via 192.168.2.1
```
- Setup linux host as router.
- Add routing table entry in host A.
- Host C can reach Host A.
````commandline
/proc/sys/net/ipv4/ip_forward
````
- Does not perist the changes across reboot.
