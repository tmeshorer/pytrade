1) Load kubeconfig

## Version
```commandline
kubectl version
```

## Config file
```commandline
KUBECONFIG
```

```commandline
$HOME/.kube/config
```

## Cascade

```commandline
kubectl delete job job1 cascade=false -n my-namespace
```

# Watch events
```yaml
kubectl get --watch
```