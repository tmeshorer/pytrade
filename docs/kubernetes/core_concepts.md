- Ships - worker nodes.
- Control ship - master nodes.
- Maintain information about the ships.
- ETCD store inforation into key/value format.
- Crane - scheduling.
- Application are form of containers.
- DNS service - container
- docker installed on all the nodes - run containers.
- Captain - kubelet - run on each node, deploy or destroy containers. 
- Kube proxy - rules on worker nodes -

# Etcd
- ./etcd
```commandline
./etcdctl set key1 val1
```
```commandline
--advertise-client-url
```

kubectl get pods -n kube-system

# KubeAPI Server
