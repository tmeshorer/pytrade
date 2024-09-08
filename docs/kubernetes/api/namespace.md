# Mission
Way of isolation

# General
- Each resource is in one namespace.
- Not all resources are namespaces (Node, PV)
- Pod in namespaced A cannot read secret from namespace B

# Special namespace
- `default`
- `kube-system` - objects created by kubernetes
- `kube-public` reserved for cluster use
- `kube-node-lease`

# How to

## Switch to ns
```commandline
kubectl config set-context --current --namespace="my-ns"
```

## View current namespace
```commandline
kubectl config view | grep namespace
```

## List all pods in all namespaces
```commandline
kubectl get pods -A
```

## Delete namespace stuck in terminating

```commandline
kubectl edit ns stuuck
```
remove entries in finalizier section

