# Overview
 - Scales the number of pods automatically on observed CPU
 - Customer / External metrics
 - Avalabile for: Replicaset / Deployment/ Stateful set

# Commands
- autoscale an hpa that mainatain an avg cpu usage of 80% across all pods
```commandline
kubectl autoscale deploy my-deployment —-min=3 —-max=10 —-cpu-percent=80
```


