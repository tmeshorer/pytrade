# Overview
- A Pod Disruption Budget limits the number of Pods of a replicated application
that are down simultaneously from voluntary disruptions. 
- I defined 3 replicas , is this enough
- PDB: maxUnavilable: 1
- Cannot delete the pod but not other ones

# Fields
- `minAvailable` - how many pods must always be available.
- `maxUnavilable` - how many pods can be evicted.

# Yaml
```yaml
spec:
  minAvailable: 1
  maxUnavailable: 1
  selector:
    matchLabels:
    app: my-app
```

# Command line
```yaml
kubectl get pdb -n my-namespace
```




