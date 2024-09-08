


```yaml
tier:backend
env:dev
app:crawler
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: labeled-pod
  labels:
    env: dev
    tier: backend
spec:
  containers:
  - image: nginx:1.25.1
    name: nginx
```
3) Check pod labels:
```yaml
 kubectl describe pod labeled-pod
```

4) Add a label
```commandline
kubectl label pod labeled-pod region=us --overwrite
```

5) Query using labels
```commandline
kubectl get pods -l 'team in (shiny, legacy)' --show-labels -w
```

6) List pods with labels:
```commandline
kubectl get pod —l app=my-app,version=v2
```

6) Used by kubernetes object

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-network-policy
spec:
  podSelector:
    matchLabels:
      tier: frontend
```

Recommended Labels

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/version: "1.25.1"
    app.kubernetes.io/component: server
spec:
  containers:
  - name: nginx
    image: nginx:1.25.1
```

### Labels
- Labels are key/value pairs that can be attached to Kubernetes objects such as Pods and ReplicaSets.
- Annotations, on the other hand, provide a storage mechanism that resembles labels: key/value pairs designed to hold nonidentifying information that tools and libraries can leverag
- Applying labels:
```yaml
 kubectl run alpaca-prod \
  --image=gcr.io/kuar-demo/kuard-amd64:blue \
  --replicas=2 \
  --labels="ver=1,app=alpaca,env=prod"
```
- See labels
```yaml 
 $ kubectl get deployments --show-labels

```
- Label selector - Label selectors are used to filter Kubernetes objects based on a set of labels. Selectors use a simple syntax for Boolean expressions
- only ver2 :
  ```commandline
  kubectl get pods --selector="ver=2"
  ```
- Labels in set of values
  ```commandline
  kubectl get pods --selector="app in (alpaca,bandicoot)"
  ```
- Here we are asking for all of the deployments with the canary label set to anything:
  ```commandline
  kubectl get deployments --selector="canary"
  ```
- In addition to enabling users to organize their infrastructure, labels play a critical role in linking various related Kubernetes objects. Kubernetes is a purposefully decoupled system. There is no hierarchy and all components operate independently. However, in many cases, objects need to relate to one another, and these relationships are defined by labels and label selectors.
- For example, ReplicaSets, which create and maintain multiple replicas of a Pod, find the Pods that they are managing via a selector. Likewise, a service load balancer finds the Pods to which it should bring traffic via a selector query. When a Pod is created, it can use a node selector to identify a particular set of nodes onto which it can be scheduled. When people want to restrict network traffic in their cluster, they use Network Policy in conjunction with specific labels to identify Pods that should or should not be allowed to communicate with each other.
- 