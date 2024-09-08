# Overview
- physical or virtual machine
- pods run on nodes
- container runtime
  - download the image
  - run the app
# Node Lifecycle
- Unkknown
- Healthy - Ready
- DiskPressure/Memory Pressure - Not Ready
- Cordoned - Ready, Scheduling Disabled

# How to
```commandline
kubectl describe node my-node
```

# Drain a node
- Debug and issue / upgrade / scale down the cluster

## Evict all pods from a node
```commandline
kubectl drain my-node
```
## Evict all pods + deamon sets
```commandline
kubectl drain my-node —-ignore-daemonsets
```

# Taint
Key/value pair associated with an effect
- `NoSchedule` - Pods that dont tolorate the taint cannot be scheduled on the Node
- `PreferNoSchedule` - Avoid schedule a pod that dont tolorate the taint
- `NoExecute` - Pods are evicted from the node if they are already running 
- 


# Cordon
Mark the node as unschedulable
```commandline
kubectl cordon my-node
$ kubectl
```
Mark the node as schedulable
```commandline
kubectl uncordon my-node
```

# Pause a node

```commandline
kubectl taint nodes my-node my-key=my-value:NoSchedule
```

# Unpause a node

```commandline
kubectl taint nodes my-node my-key:NoSchedule-
```

# Schedule
- Create a pod that can be schedule on a node who have taint:

```yaml
spec:
tolerations:
- key: "specialkey"
  operator: "Equal"
  value: "specialvalue"
  effect: "NoExecute"
```

# Pod stay bound
Delay Pod eviction
```yaml
spec:
tolerations:
- key: "my-key"
  operator: "Equal"
  value: "my-value"
  effect: "NoExecute"
  tolerationSeconds: 6000
```
# NodeController
Automatically taint a node:
- Node not ready
- Node not reachable
- Out of disk
- Network unrelaible. 



## Node heartbeat
- update to node status (kubelet)
- lease object