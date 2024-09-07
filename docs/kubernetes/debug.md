# To read
- Taint based eviction 
https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions
https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-nodes-by-condition
- 

# Nodes
1) Marking a node as unschedulable prevents the scheduler from placing new pods onto that Node but does not affect existing Pods on the Node. This is useful as a preparatory step before a node reboot or other maintenance.
```yaml
kubectl cordon $NODENAME
```
# Node Status
```yaml
kubectl describe node <name>
```
## Addresses
  - Hostname
  - ExternalIP - IP address that node is extrnaly routable
  - Internal IP.
## Condition
   Node conditions - Ready/DiskPressure/MemoryPressure/PIDPressure/NetworkUnavailable.
## Capacity
   Node have capacity - CPU / Memory / max number of pods.
## Allocatable

6) Each node has associated lease object.
4) Cordon nodes are marked as unschelable in thier spec.
5) If the node status is unknown, the scheduler will asssign them Taint:
  - node.kubernetes.io/unreachable taint, for an Unknown status, or a node.kubernetes.io/not-ready taint, for a False status,
6) Existing Pods might be evicted. 
7) Pods might have toloration

9) Heartbeat
  - Kubelet update the node `status`
  - Kubelet create and update the Lease object every 10 secs. 
  - 

# Nodes to control plane comm
## API Server to kubelet
- Fetch logs for pods
- Attach to running pod
- Provide kubelet port forwarding functionlity.
- 

# Container
## Image
- Represent binary data of all application and thier dependency.
- Image can include registry name. Default : docker public registry.
- Image Pull policy
  - `IfNotPresent` - image is pulled only if not present
  -  `Always` - every time the kubeles lunches a container.
  -  `Never` - kubelet does not try fetching the image.
- ImagePullBackOff
  - container did not start because kubernetes cannot pull the image.
  - private registry. Invalid ImagePullSecret

# Workload
# Storage
# Networking
# Configuration



# Debug Pod

## Describe pod
```yaml
kubectl describe pods <pod>
```
- are all containers running, was there a recent restart
- If Pod is `PENDING`
  - no resource to run it.
    - delete pod
    - adjust resource requests
    - or add a new node
  - Bind to <host port>
    - Use service port
- If Pod is `WAITING`
  - Failed to pull image
    - image name correct
    - pushed the image to registery
    - Try `docker pull`
- If Pod is `TERMINATING`
  - Cannot be deleted - finalizier
  - Check ValidatingWebhookConfiguration / MutatingWebhookConfiguation with UPDATE for POD

### Pod is running, but not behaving
- Delete and create with validate option
```yaml
kubectl apply --validate -f mypod.yaml
```
- Compare the Pod to the one in the api server
```yaml
ubectl get pods/mypod -o yaml > mypod-on-apiserver.yaml
```
### Debug Running Pod

- Get the pods
```yaml
kubectl get pods
```

- Describe Pod
```yaml
kubectl describe pod nginx-deployment-67d4bdd6f5-w6kd7
```
- container state: `Waiting` / `Running` / `Terminated` 
- 