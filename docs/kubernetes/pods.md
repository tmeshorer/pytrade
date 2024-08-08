Pod
----
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:blue
      name: kuard
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
```
- show desired state
- create pod
```commandline
kubectl apply -f kuard-pod.yaml
  ```
The Kubernetes system will then schedule that Pod to run on a healthy node in the cluster, where the kubelet daemon will monitor it
- List pods
```commandline
kubectl get pods
```
- In addition to the number of ready containers (1/1), the output also shows the status, the number of times the Pod was restarted, and the age of the Pod.
- More information
```commandline
kubectl get pods -o wide
```
- Text
```commandline
kubectl get pods -o yaml
```
- Pod details
```commandline
kubectl describe pods kuard
```

- Delete a pod
```commandline
kubectl delete pods/kuard
```

## Debug the pod
```commandline
kubectl logs kuard
```

- Running command in the container
```commandline
kubectl exec kuard -- date
```

- Interactive session
```commandline
kubectl exec -it kuard -- ash
```

### Application health check
Defined per container. 
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:blue
      name: kuard
      livenessProbe:
        httpGet:
          path: /healthy
          port: 8080
        initialDelaySeconds: 5
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP

```
- Liveness determines if an application is running properly. Containers that fail liveness checks are restarted. Readiness describes when a container is ready to serve user requests. Containers that fail readiness checks are removed from service load balancers
- Startup probes enable you to poll slowly for a slow-starting container while also enabling a responsive liveness check once the slow-starting container has initialized.
- Advanced Probe: `tcpSocket`, `exec` probe.

### Resource Management
- Ensure the nodes are packed.
- Kubernetes guarantees that these resources are available to the Pod
- Kubernetes allows users to specify two different resource metrics. Resource requests specify the minimum amount of a resource required to run the application. Resource limits specify the maximum amount of a resource that an application can consume
- Resources are requested per container.
- Requests are used when scheduling Pods to nodes. The Kubernetes scheduler will ensure that the sum of all requests of all Pods on a node does not exceed the capacity of the node. Therefore, a Pod is guaranteed to have at least the requested resources when running on the node. Importantly, “request” specifies a minimum. It does not specify a maximum cap on the resources a Pod may use. To explore what this means, let’s look at an example.
- Memory requests are handled similarly to CPU, but there is an important difference. If a container is over its memory request, the OS can’t just remove memory from the process, because it’s been allocated. Consequently, when the system runs out of memory, the kubelet terminates containers whose memory usage is greater than their requested memory. These containers are automatically restarted, but with less available memory on the machine for the container to consume.
- In addition to setting the resources required by a Pod, which establishes the minimum resources available to it, you can also set a maximum on a its resource usage via resource limits.
- ```yaml- 
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:blue
      name: kuard
      resources:
        requests:
          cpu: "500m"
          memory: "128Mi"
        limits:
          cpu: "1000m"
          memory: "256Mi"
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
- ```
## Volumes
- support persistent data
- To add a volume to a Pod manifest, there are two new stanzas to add to our configuration. The first is a new spec.volumes section. This array defines all of the volumes that may be accessed by containers in the Pod manifest. It’s important to note that not all containers are required to mount all volumes defined in the Pod. The second addition is the volumeMounts array in the container definition. This array defines the volumes that are mounted into a particular container and the path where each volume should be mounted. Note that two different containers in a Pod can mount the same volume at different mount paths.
 
 ```yaml
 apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  volumes:
    - name: "kuard-data"
      hostPath:
        path: "/var/lib/kuard"
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:blue
      name: kuard
      volumeMounts:
        - mountPath: "/data"
          name: "kuard-data"
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
 
```
- Types of volumnes:
  - Commounication
  - Synchronization
  - Cache
  - Persistent data (NFS)
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