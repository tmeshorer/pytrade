- CRI -container runtime.
- Usually ship with containerd.
- gVisor / Kata / Spin
- K8s cluster - one or more nodes, providing CPU/Memory/other resources.
- Control plane nodes - 3 for HA. Api server, scheduler, controllers.
- Worker nodes - running the apps.
- Control plan - brain - schedule tasks, implement self healing.
  - API Server - front end of kubernetes. REST API over HTTPS. All request pass auth/authz.
  - Cluster store - store the desired state. etcd.
  - Controller - implement inteliigence (Replica set controller)
  - Scheduler - watch api server fo rnew tasks, identify cabale node, assign tasks to nodes.
  - Scheduler - check taint / affinity / anti affinity. Mark task as pending if cannot find one.
- Worker Node
  - Kubelet - watch API/ instruct runtime to execute task/ report status to api server.
  - Runtime - pull container image/ manages container lifecycle.
  - Kube proxy - implement balance/traffic.
- Package app in a Pod. Give the pod to k8s.
- Run the app as deployment.
  - container wrap the app
  - pod wraps the container
  - deployment wrap the pod - self healing, scaling
- Declarative model - describ the desired state, controller see the observed state and reconcile.
- Post the manifest via kubectl.
- Atomic Unit - Pod (vs container in docker). K8s can run VM but need to be in a Pod.
- Multi container pod - share network, volume
- Pods are basic unit of scaling.
- Pods are immutable.
- Pod deployed with Deployment/StatefulSet/DeamonSet.
- Rollout replace old Pods with new ones.
- Scaling up add new Pods
- Scaling down delete existing Pod
- Service provide relaiable IP. Frontend - DNS name, IP address, network port.
- Pod share:
  - file system
  - network stack
  - memory
  - process tree
  - hostname
- Nodes are host servers (Physical machine / VM)
- Pod scheduling features:
  - node selector - run pod on a specific node
  - Affinity rules attract
  - Anti affinity rept.
  - Hard/soft tules.
- Resurce request and limit - Tell the scheduler how much CPI and memoty Pod need.
- Pod life cycle - Mortal.
   - Pending - scheduler search for node. find it, kubelet start it
   - All container running - Running
   - In long running (webserver) it is running. In short running It succeed.
   - KubeVirt - VirtualMachineInstance
 - Deployment start a new Pod, Node evection. Scaling - new Pod. We replace a Pod. 
 - Kubernetesd restart containers.
 - Pod usually started by a Workload resource.
 - Pod network - k8s automatically connect all pods to it. Implemented by CNI interface.
 - Pod network is only for pods not Nodes.
 - Multi containers
   - init container - start and complete before the application
   - Side car container - regular container that run at the same time.

# Namespaces
- parition k8s cluster into virtual cluster.
- Some object are note namespaced: Nodes, PersistentVolume
```commandline
kubectl get api-resources
``` 
- create ns: finance / hr / coporate-ops. 
- ns vs multiple clusters.
- default namespace.
- kube-system namespaces
- set current namespace:
```commandline
 kubectl config set-context --current --namespace shield
```

1) Deployment - scale, rollup, rolldown.
2) Deployment manages one or more identical pods.
3) Auto scaling:
   - Horizontal Pod Autoscaler
   - Vertical Pod Autoscaler
   - Cluster Autoscaler.
4) Deployment create two ReplicaSet old and new. And adjust the replicas.
5) spec.selector - label pod need to have to be managed.
6) Kubernetes treat Pods and unraliable. 

