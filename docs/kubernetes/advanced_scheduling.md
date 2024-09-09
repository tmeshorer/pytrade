Commands
--------
```commandline
kubectl run <>
```
```commandline
kubectl cluster-info
```
```commandline
kubectl get nodes
kubectl get pods
```

- scale - add more pods / more nodes.
- pods can have multi containers.

- View command inside a pod:

```commandline
k -n eee exec -it app -- cat /log
```
- Replace a pod
```commandline
kubectl replace --force -f /tmp.yaml
```


How the Scheduler works in Kubernetes
Filters and predicates
nodeSelector
Node affinity
Pod affinity/anti-affinity
Taints and tolerations
Topology Spread Constraints
Custom schedulers

Persistance
----
Managing configurations
Managing secrets
Using Kubernetes Volumes
Creating Persistent Volumes
Creating Persistent Volume Claims
Provisioning volumes dynamically
Managing stateful applications
Deploying a single database with persistence
Deploying a clustered database with persistence

Apply
-----
```commandline
kubectl apply -f test.yaml"
```
1) Validate the resource
2) Convert Yaml to Json
3) Read the config from KUBECONFIG
4) Send the request to `kube-apiserver`

on the server
-------------
1) API server authenticate the request
2) Check RBAC to see if you have permissions
3) Object intercept by admission-cotroller

Namespace lifecycle adminnsion controller.

MutationAdmissionController
-------
1) Add storage class.
2) 