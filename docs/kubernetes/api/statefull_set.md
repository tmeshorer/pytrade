# Overview
- Container for statefull apps.
- Each pod have a name:
  - web - 0
  - web - 1
  - web - 2
- Provide the furntee about the uniqeness of these pods
- Maintain a sticky identity for each of the pods
- Each created pod have its own PV and auto created PVC
- Deleting and calcing statefull set does not delete the volumes
## Yaml
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
name: web
spec:
  serviceName: "nginx"
  replicas: 3
    selector:
      matchLabels:
          app: nginx
    template:
      metadata:
        labels:
          app: nginx
        spec:
          containers:
            - name: nginx
              image: nginx
              ports:
                - containerPort: 80
              name: web
      volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
          volumeClaimTemplates:
            - metadata:
              name: www
                spec:
                  accessModes: [ "ReadWriteOncePod" ]
                  resources:
requests:
storage: 1Gi
```