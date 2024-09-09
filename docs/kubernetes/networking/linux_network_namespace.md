# Namespaces
- Rooms in the house assign to children. 
- Cannot see what happen outside the room. 
- Underlying host can
- We see different process id, 
```commandline
ps aux
```

## Networking namespace
- our host has routing table
- contain have virtual interfaces,
```commandline
ip netns add red
ip netns add blue
```

```commandline
ip link
```
## Inside the namespace
```commandline
ip netns exec red ip link
```
- same is true with ARP tables.
- same for routing spaces.
- connectiviy between the namespaces.
- connect two namespace using virtual cable. 
```commandline
ip link set veth-red netns red.
```
- assign ip address to each netspaces.
- create a virtual switch 
- linux bridge. 
```commandline
ip link add v-net-0 type bridge.
```
- connect all virtual cables to the bridge.
```commandline
iplink add
```

add route entry to local host is the gateway.