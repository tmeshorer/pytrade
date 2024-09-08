# Overview
- Seperate configuration from pods
- Allow different apps in different environments

# Create configmap from key and value

```commandline
kubectl create cm my-cm-1 —-from-literal=my-key=my-value -n my-namespace
```

# Create a Pod with ConfigMap mounted as volume

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
    containers:
      - name: my-container
    image: busybox
    volumeMounts:
      - name: my-cm-volume
    mountPath: /etc/myfile.txt
    volumes:
      - name: my-cm-volume
    configMap:
      name: config 73
```