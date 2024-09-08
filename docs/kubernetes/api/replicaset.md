## Replica set

Create Pods according to the number of specified replica

### Reconicliation loops

The central concept behind a reconciliation loop is the notion of desired state versus observed or current state. Desired state is the state you want. With a ReplicaSet, it is the desired number of replicas and the definition of the Pod to replicate. For example, “the desired state is that there are three replicas of a Pod running the kuard server.” In contrast, the current state is the currently observed state of the system. For example, “there are only two kuard Pods currently running.”

### Relating pods and replica set
 Though ReplicaSets create and manage Pods, they do not own the Pods they create. ReplicaSets use label queries to identify the set of Pods they should be managing
 
ReplicaSets are designed to represent a single, scalable microservice inside your architecture. Their key characteristic is that every Pod the ReplicaSet controller creates is entirely homogeneous. Typically, these Pods are then fronted by a Kubernetes service load balancer, which spreads traffic across the Pods that make up the service. Generally speaking, ReplicaSets are designed for stateless (or nearly stateless) services

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  labels:
    app: kuard
    version: "2"
  name: kuard
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kuard
      version: "2"
  template:
    metadata:
      labels:
        app: kuard
        version: "2"
    spec:
      containers:
        - name: kuard
          image: "gcr.io/kuar-demo/kuard-amd64:green"
```
- Kubernetes create the pod from the template
-  ReplicaSets monitor cluster state using a set of Pod labels to filter Pod listings and track Pods running within a cluste

### Kubectl
```commandline
kubectl apply -f kuard-rs.yaml
```
```commandline
 kubectl describe rs kuard
```

Set of pods for replica set
```commandline
kubectl get pods -l app=kuard,version=2
```

Scaling the replica set
```commandline
kubectl scale replicasets kuard --replicas=4
```

### Autoscaling

```commandline
 kubectl autoscale rs kuard --min=2 --max=5 --cpu-percent=80
```

```commandline
kubectl get hpa
```