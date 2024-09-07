# Overview
- Data persist behind the lifecycle of pod/volume
- PersistentVolume - piece of storage in k8s cluster
- PersistentVolumeClaim - Request the resource of persistent volume. 
- Dynamic allocation via persistent volume class. 

# YAML
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: db-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /data/db
```

# Option

- Persistent volumn options.
  - `spec.volumeMode` - FileSystem(mounts the volume into a director)
  - `spec.volumeMode` - Block - mount the volume as a raw block device.
- Access mode
  - `ReadWriteOnce` - Read/write access by a single node
  - `ReadOnlyMany` - Read only access by many nodes
  - `ReadWriteMany` - Read/Write access by many node
  - `ReadWriteOncePod` - R/W access mounted by a single pod.
- Reclaim policy (Specify what should happen to persistent volume when claim is deleted)
  - `Retain` - PersistentVolume is "released"
  - `Delete` - Remove the persistent volume and associate storage.