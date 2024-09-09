# Mission
Way of isolation

# General
- Each resource is in one namespace.
- Not all resources are namespaces (Node, PV)
- Pod in namespaced A cannot read secret from namespace B
- Create your own namespace.
- Can have ResourceLimits
- Resource within a namespace - use name. 
- Appdne the name of the name space to the name of the service.
- namespace dev
```yaml
db-service.dev.svc.cluster.local 
```
- move the namespace definition into the file.

```commandline
kubectl get pods -n x
```

# set namespace

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

# Resource Quota for namespace

```yaml
apiVersion: v1
kind: ResourceQuota
metadata: 
  name: compute-quata
  namespace: dev
spec:
  hard:
    pods: "10"
    request.cpu : "4"
    requests.memory: 5Gi
```
