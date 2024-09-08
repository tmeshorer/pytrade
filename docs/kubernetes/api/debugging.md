# Process

## Show information about all pods
```commandline
kubectl get pod -n my-ns
```

## Show information about a pod
```commandline
kubectl describe pod my-pod -n my-ns
```

## CrashLoopBackOff

## Pod Stuck in Pending
- Pod cannot be scheduled
  - Resource limit
  - Add node capacity
  - Add more nodes

# Show cluster error message

## Display all events in a namespaces
```commandline
kubectl get events -n my-ns
```

## Display only warning message
```commandline
kubectl events --field-selector type=Warning
```

## Pod Study in Waiting /ImagePullBackOff status

Solutions:
- Image / Tag / URL are good ?
- Image exist in docker registry ?
- Can you pull the image ?
- K8s has permission to pull the image ?
- ImagePullSecret ?


# Kubernetes debug
- Run an epemeral container near the pod you want to debug
- In this container run curl / wget

```commandline
kubectl debug my-pod -it —-image=busybox —-target=my-pod —-container=my-debug-container
```

- Share the process namespace with a container inside the pod
- Can see all the processes create by my-pod

# Pod restart
- OOMKiller - Pod uses too much memory
- Define request and limit memory

# Pod cant start
# `RunContainerErr` / `ContainerCreating`
# Broken link to configmap or a secret

# Pod is running but not working
```commandline
kubectl logs my-pod
```

# Container is restarting
- Liveness probe is wrong

# Access the pod without an external load balancer
```commandline
kubectl port-forward my-pod 8080
```

Mount a tunnel to the service
```commandline
kubectl port-forward svc/my-svc 5050
```


