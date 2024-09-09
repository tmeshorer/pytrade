# Single docker host
## None network
```commandline
docker run --network none nginx
```
## Host network
Container attach to host network
```commandline
docker run --network host nginx
```

# Bridge
- Internal private network is created 172.17.0.0, each device.
```commandline
docker netowrk ls
```
On the host, docker0. The interface is down, the bridge network is done.
Switch to then namespaces within the host.

# Container create
```commandline
ip netns
```
```commandline
docker run ngnix
```
docker attach network namespace to the bridge
- create virtual table

# To expose service
- docker provide port mapping
```commandline
docker run -p 8080:80 nginx.
```
How does docker forward traffic from 8080 to 80.
Docker update the IP tables.

