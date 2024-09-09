# Background
- Old `Volume`, user need to configure storage in pod def file.
- Like to configure storage, independently. 
- PV - cluster wide persisent volume
- Use use `PersistenVolumeClaim`


# Overview
- Pods are mortal as well as nodes.
- To store data permanently, use `PersistentVolume`
- To requet phsical storage create `PersisentVolumeClaim`
- without storage class: Pod-> volume -> PVC -> PV -> storage.
- with storage class: Pod->volume->PVC->StorageClass->(dynamic create)PV
- Data persist behind the lifecycle of pod/volume
- PersistentVolume - piece of storage in k8s cluster, store the data
- PersistentVolumeClaim - Request the resource of persistent volume. 
- Dynamic allocation via persistent volume class. 
- Provide storage location.
- Does not belong to a namespace
- Support differnet storage type (NFS.
- After creation, status is available, not bound to any PVC
- 

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
  - `spec.volumeMode` - FileSystem(mounts the volume into a directory)
  - `spec.volumeMode` - Block - mount the volume as a raw block device.
- Access mode (How volume should be mounted on the host)
  - `ReadWriteOnce` - Read/write access by a single node
  - `ReadOnlyMany` - Read only access by many nodes
  - `ReadWriteMany` - Read/Write access by many node
  - `ReadWriteOncePod` - R/W access mounted by a single pod.
- Reclaim policy (Specify what should happen to persistent volume when claim is deleted)
  - `Retain` - PersistentVolume is "released". PV is not deleted if the user deletes the PVC.
               Status of PV will change to Released.
  - `Delete` - Remove the persistent volume and associate storage.