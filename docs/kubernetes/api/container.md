# ImagePullPolicy
- IfNotPresent - does not pull the image
- Always - pulled anytime the pod start
- Never - no attempt is made to pull the images

## Image pull secret
```yaml
containers:
- name: my-container
  image: my-registry.com/my-app:tag
  imagePullPolicy: Always
  imagePullSecrets:
- name: registry-secret

```

### Registry image secret

```commandline
kubectl create secret docker-registry registry-secret
—-docker-server=<host>:8500
—-docker-username=<user_name>
—-docker-password=<user_password>
—-docker-email=<user_email>
```

# Request/Limit
- If a Pod uses too much memory, OOM Killer can destroy them
- OOM Killer run on each node.
- In order to avoid, defines `request` / `limit`
```yaml
resources:
  requests:
    memory: 64Mi
    cpu: 250m
  limit:
    memory: 128Mi
    cpu: 500m
```

- Scheduer use this to descice which node host the pod
- Request - min needed for pod to be scheduled.
- Limit - Limit max usage
- Once a cpu reach limit it will keep running
- Once container reach memory it will be terminated.

# Create request / limits

```yaml
resources:
    requests:
      memory: 64Mi
      cpu: 250m
    limit:
      memory: 128Mi
      cpu: 500m
```

# Top
- display pod memory and cpu consumption
```commandline
kubectl top pod
```
- display containers memory and cpu consumption
```commandline
kubectl top pod --containers
```
- display nodes memory & cpu consumption
```commandline
kubectl top node
```
