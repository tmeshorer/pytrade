# Overview
- Claim a suite PersistenVolume
- Pod uses pvc to request pyhsical storage
- After PVC deployment, controlplan searches suitable PV with the same `StorageClass`
- PV is found, PVC is attached, PV status is bound.
- K8s bind the persistent volume to claim. 
- Can still use labels and selector. Smaller claim can be bound to bigger volume. 
- PVC remain pending , until new volume are remain available volume.
- PVC will get the whole volume size
 
```commandline
kubectl get pvc    
```

```commandline
kubectl delete pvc <>    
```
Persistent volume will retain, is not available for reuse. Or set to 'Delete', or 'Recycle'



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

