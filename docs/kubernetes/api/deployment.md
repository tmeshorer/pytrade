# Overview

- Handle pod creation
- Create `ReplicaSet` and ensure that they are running

## Features
- Rolling update/ Rollout
- Deployment History

The Deployment object exists to manage the release of new versions. Deployments represent deployed applications in a way that transcends any particular version. Additionally, Deployments enable you to easily move from one version of your code to the next. This “rollout” process is specifiable and careful. It waits for a user-configurable amount of time between upgrading individual Pods. It also uses health checks to ensure that the new version of the application is operating correctly and stops the deployment if too many failures occur.

## Create
### CLI
```commandline
kubec create deploy my-deply --image ngnix
```

Scale:
```commandline
kubectl scale deploy my-deploy --replicas=5 
```

Apply:
```commandline
kubectl apply -f my-deploy.yaml
```

Update deployment:
```commandline
kubectl set image deploy my-deply busybox=busybox:1.36.0 --record
```

Show rollout:
```commandline
kubectl rollout status deploy my-deploy
```

Show histody of deployment:
```commandline
kubectl rollout history deploy my-deploy
```

Rollbacl:
```commandline
kubectl rollout undo deploy my-deploy
```

Restart:
```commandline
kubectl rollout restart deploy my-deploy
```

Pause and resume:
```commandline
kubectl rollout pause deploy
kubectl rollout resume deploy
```

### Yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kuard
  labels:
    run: kuard
spec:
  selector:
    matchLabels:
      run: kuard
  replicas: 1
  template:
    metadata:
      labels:
        run: kuard
    spec:
      containers:
      - name: kuard
        image: gcr.io/kuar-demo/kuard-amd64:blue
```

- Deployment manage ReplicaSet, Replica set manage pods
```commandline
kubectl get replicasets --selector=run=kuard
``` 



### Starategy

```yaml
strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
```

The strategy object dictates the different ways in which a rollout of new software can proceed. 
There are two strategies supported by Deployments: Recreate and RollingUpdate. 
These are discussed in detail later in this chapter.

### Scaling the deployment

```commandline
kubectl get deployments kuard
```

### Update the container image

```yaml
 containers:
   - image: gcr.io/kuar-demo/kuard-amd64:green
     imagePullPolicy: Always
```

To see the rollpout status:

```yaml
kubectl rollout status deployments kuard
```

Rollout history
```yaml
kubectl rollout history deployment kuard
```

### Recreate strategy
Should only be used for test deployment
The Recreate strategy is the simpler of the two. It simply updates the ReplicaSet it manages to use the new image and terminates all of the Pods associated with the Deployment. The ReplicaSet notices that it no longer has any replicas and re-creates all Pods using the new image. Once the Pods are re-created, they are running the new version.

### Rolling update

As you might infer from the name, the RollingUpdate strategy works by updating a few Pods at a time, moving incrementally until all of the Pods are running the new version of your software.

Configuration

The maxUnavailable parameter sets the maximum number of Pods that can be unavailable during a rolling update. It can either be set to an absolute number (e.g., 3, meaning a maximum of three Pods can be unavailable) or to a percentage (e.g., 20%, meaning a maximum of 20% of the desired number of replicas can be unavailable). Generally speaking, using a percentage is a good approach for most services, since the value is correctly applied regardless of the desired number of replicas in the Deployment. However, there are times when you may want to use an absolute number (e.g., limiting the maximum unavailable Pods to one).

maxSurge

The maxSurge parameter controls how many extra resources can be created to achieve a rollout. To illustrate how this works, imagine a service with 10 replicas. We set maxUnavailable to 0 and maxSurge to 20%. The first thing the rollout will do is scale the new ReplicaSet up by 2 replicas, for a total of 12 (120%) in the service. It will then scale the old ReplicaSet down to 8 replicas, for a total of 10 (8 old, 2 new) in the service. This process proceeds until the rollout is complete. At any time, the capacity of the service is guaranteed to be at least 100% and the maximum extra resources used for the rollout are limited to an additional 20% of all resources.