# Overview
- Claim a suite PersistenVolume
- Pod uses pvc to request pyhsical storage
- After PVC deployment, controlplan searches suitable PV with the same `StorageClass`
- PV is found, PVC is attached, PV status is bound.
- 


# Yaml
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: db-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ""
  resources:
    requests:
      storage: 256Mi
```

# Get
```commandline
kubectl get pvc db-pvc
```

# Mount into a pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-consuming-pvc
spec:
  volumes:
  - name: app-storage
    persistentVolumeClaim:
      claimName: db-pvc
  containers:
  - image: alpine:3.18.2
    name: app
    command: ["/bin/sh"]
    args: ["-c", "while true; do sleep 60; done;"]
    volumeMounts:
      - mountPath: "/mnt/data"
        name: app-storage
```

