# Mission
Find a suitable node for a new Pod. When a pod is created it is in `PENDING`
Select a worker node.


## Nodes
- add labels to nodes
## Node selector  
- define nodes selector. I want to run in a node with label "node=mynode"
```yaml
nodeSelector:
  node: my-node
```
Label node
```commandline
kubectl label nodes <node-name> key=value
```
- Limitation - only one label, cannot achive that. 
## Node Affinity
Like selector but with more expressive syntax
- Hard rule
- Soft rule
- Operator: In, Exist, Gt, Lt...
  - `Exist` - check if the key exist.
 - requireDuringScheduleing
 - during scheduling - where a pod does not exist and created for the first time.
 - require - if cannot find one the pod will not be schedules.
 - preffered - if not node found, the scheduler will place the node on matching node.
 - `DuringExecution` - change has been made in the environment.  `Ignore` any changes will not affect them
## Pod Affinity
Allow to run the Pod on the same Node than another Pod. Usefull for pods that need to 
run on the same machine.
```yaml
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        nodeSelectTerms: 
            - matchExpressions:
              - key: app
                operator: In
                values:
                  - my-app
```
## Pod anti-affinity
Allow to run several replicas of a deployment on different node
```yaml
affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
          matchExpressions:
            - key: app
              operator: In
              values:
                - my-app
          topologyKey: kubernetes.io/hostname
```




# Tools
## Quality Of Service
Depdending on request and limits, the POD is classified into QOS class
### Guarnteed
- Assigned to nodes which have enough resources.
- Pod gurnteed not to be killed until they exceed thier limit
- Requests and limits must be equal
```yaml
resources:
  requests:
     memory: "64Mi"
     cpu: "20m"
  limit:
     memory: "64Mi"
     cpu: "20m"
```
### Burstable
- When reached thier limit killed before Gurnteed nodes.
- At least one container in the Pod must have mem or cpu defined
### Best Efforts
- Containers can use any amount of free memory and CPU
- Killed first if there are not enough resources.
- If requests and limits are not set for all containers. 
 



## Taints and Toloration
- Taint belong to a node. prevent pods from being placed on a node.
- Tolorant - put on pods - pod D is tollorant to node taint.

### Tainted
```commandline
kubectl taint nodes node-name 
```
- Taint affect
  - NoSchedule - no pod will be scheduled.
  - PrefferedNoSchedule
  - NoExecute - new pods will not be scheudle. Existing pods will be evicted.
- Taint is set on the master node, to prevent any node.

## Toloration
Added to the pod yaml file
```yaml
tolorations:
  - key: "app"
  - operator: "Equal"
  - value: "blue"
  - effect: "NoSchedule"
```

## Resource Limits
## Resource Requests
- The scheduler assure that the sum of all resource request is less than node capacity
- Sum of resource limit > node capacity than we have overcommitment.
- Pod placed on a node consume resources. 
- No resources: Insufficient CPU. 
## Request 
  ```yaml
    resources:
      requests:
        memory: "4Gi"
        cpu: 1
  ```
- What does one count of CPU means: 100m, can go as low as 1m
- one count of cpu is 1 core / 1 VCPU. 
- Memory : `256Mi`. G / Gi (Gibibyte)
- Container can conume as much as it wants. Set a limit 1 vcpu. 
### Limits
  ```yaml
    resources:
      limits:
        memory: "2Gi"
        cpu: 1
  ```
- Each containers have request and limit.
- The system trotale the cpu if container pass the limit. 
- The pod will terminate - OOM error.

### Default Behavior CPU
- Any pod can saffocate the nodes.
- If request is not specified, k8s set request to limit.
- Not good to set cpu limit,
- Set request but not limit. (Ideal)
- Pod must have requests if we do not set limit. 
### LimitRange
Define default limit, and default range. 
Can create limit range for memory and cpu
### Create resource quota 
- Hard limit per namespace.
- 

### CPU
- Scheduler use this to find a node. IF not found it can evict pods based on QOS and Pod prioity.
- Resource request are the relative share of the CPU.
- CPU request are weighted.
- If not resource request for CPU, dont get any CPU (2).
- CPU limits are trootled. 
### Memory
- Each process can see all memory
- But working set is max, otherwise will see OOM kill
- 
## Horizontal Pod Autoscaler
- Notice high load with k8s kubernetes server.
- Handle load:
  - Add more pods (HPA)
  - Increate resource (VPA)
  - Add more nodes (cluster autoscaler)
- HPA automatically scales the number of pods in deployment or stateful set.
## Vertical Pod Autoscaler
- Update the requests based on load.
- Maintain a ratio between request and limits.
## Cluster Auto scaler
- Automatically adjust the size of kubernetes cluster.
- Based on `Pending` pods
- 
## Fair scheduler
## ControlGroup
## Troubleshot
`Pending` means that the cluster run out of resources.

 

## Pod in PENDING
- cluster is full
- Pod has special constraints
- Scheduler is not running

