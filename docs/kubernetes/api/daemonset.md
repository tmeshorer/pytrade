# Deamonset

- A DaemonSet ensures that a copy of a Pod is running across a set of nodes in a Kubernetes cluster. DaemonSets are used to deploy system daemons such as log collectors and monitoring agents
- Manages by the deamon set controller.
- On each pod, set the nodeName. 
- Deamonset use default affinity rule
- Monitoring agent
- Log collector
- If a new node is added to the cluster, then the DaemonSet controller notices that it is missing a Pod and adds the Pod to the new node.
- Yaml:
```yaml

apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  labels:
    app: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluent/fluentd:v0.14.10
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/lo
```

## Limit to specific nodes

- Label a node:  kubectl label nodes k0-default-pool-35609c18-z7tb ssd=true
- Node selectors can be used to limit what nodes a Pod can run on in a given Kubernetes cluster
- Daemonset:

```yaml
apiVersion: apps/v1
kind: "DaemonSet"
metadata:
  labels:
    app: nginx
    ssd: "true"
  name: nginx-fast-storage
spec:
  selector:
    matchLabels:
      app: nginx
      ssd: "true"
  template:
    metadata:
      labels:
        app: nginx
        ssd: "true"
    spec:
      nodeSelector:
        ssd: "true"
      containers:
        - name: nginx
          image: nginx:1.10.0
```

Only on desired nodes
```yaml
  nodeSelector:
  my-key: my-value
```

# Static Pod

- What if there is no node, no control plane
- Can the kubelet operate as stand alone.
- Put the pod definition files on:
- /etc/kubernetes/manifests
- Kubelet will also recreate the pods.
- API server aware of static pods.
- Kubelet create the static pod in the api server (View only)
- Control plan components are pods.
- Static Pod - create by kubelet. Deamonset create by the api server.

# Can have multiple scheduler
- KubeSchedulerConfiguration
- 