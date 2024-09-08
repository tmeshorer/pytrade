# Mission
Find a suitable node for a new Pod. When a pod is created it is in `PENDING`
Select a worker node.

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
- 



## Taints and Toloration


## Resource Limits
## Resource Requests
- The scheduler assure that the sum of all resource request is less than node capacity
- Sum of resource limit > node capacity than we have overcommitment.
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

