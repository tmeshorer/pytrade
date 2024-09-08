# Overview
- In order to setup dynamic provisioning
- GCEPersistentDisk / AzureDisk/ AwsEBS
- VolumeBindingMode: Immediate - means that volume binding & dynamic provisioning will occur
  when the PVC is created.
- 

# Yaml
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
  replication-type: regional-pd
```
# Use storage class

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: db-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 512Mi
  storageClassName: standard
```
