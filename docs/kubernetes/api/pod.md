# Definion

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hazelcast                      1
  labels:                              2
    app: hazelcast
    env: prod
spec:
  containers:
  - name: hazelcast
    image: hazelcast/hazelcast:5.1.7   3
    env:                               4
    - name: DNS_DOMAIN
      value: cluster
    ports:
    - containerPort: 5701              
```

# Create from manifest
```yaml
kubectl apply -f pod.yaml
```

# List Pods
```yaml
kubectl get pods
```

# Pods States
- Pending - Pod accepeted by k8s. One or more container images were created
- Running - At least one container running
- Succeed - All container terminated successfuly
- Failed - At least one container failed with and error
- Unknown - The state of the pod is unknown.

# Show pods details
```yaml
kubectl describe pods hazelcast
```

# Show pods logs
```yaml
kubectl logs hazelcast
```

## Pod IP Address
1) Every pod is assigned an IP
2) The IP address assigned to a Pod is unique across all nodes and namespaces. This is achieved by assigning a dedicated subnet to each node when registering it. When creating a new Pod on a node, the IP address is leased from the assigned subnet. This is handled by the networking life cycle manager kube-proxy along with the Domain Name Service (DNS) and the Container Network Interface (CNI).
3) It’s important to understand that the IP address is not considered stable over time. A Pod restart leases a new IP address. Therefore, this IP address is often referred to as virtual IP address.

## Pod configuration
1) Add env var:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: spring-boot-app
spec:
  containers:
  - name: spring-boot-app
    image: bmuschko/spring-boot-app:1.5.3
    env:
    - name: SPRING_PROFILES_ACTIVE
      value: prod
    - name: VERSION
      value: '1.5.3'
```
2) Pass command line args

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: busybox:1.36.1
    command: ["/bin/sh"]
    args: ["-c", "while true; do date; sleep 10; done"]
```

# Multi container
- init container
- side car

## Init container


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: business-app
spec:
  initContainers:
  - name: configurer
    image: busybox:1.36.1
    command: ['sh', '-c', 'echo Configuring application... && \
              mkdir -p /usr/shared/app && echo -e "{\"dbConfig\": \
              {\"host\":\"localhost\",\"port\":5432,\"dbName\":\"customers\"}}" \
              > /usr/shared/app/config.json']
    volumeMounts:
    - name: configdir
      mountPath: "/usr/shared/app"
  containers:
  - image: bmuschko/nodejs-read-config:1.0.0
    name: web
    ports:
    - containerPort: 8080
    volumeMounts:
    - name: configdir
      mountPath: "/usr/shared/app"
  volumes:
  - name: configdir
    emptyDir: {}

```

Get Log:
```commandline
kubectl logs business-app -c configurer
```

## Sidecar


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: webserver
spec:
  containers:
  - name: nginx
    image: nginx:1.25.1
    volumeMounts:
    - name: logs-vol
      mountPath: /var/log/nginx
  - name: sidecar
    image: busybox:1.36.1
    command: ["sh","-c","while true; do if [ \"$(cat /var/log/nginx/error.log \
              | grep 'error')\" != \"\" ]; then echo 'Error discovered!'; fi; \
              sleep 10; done"]
    volumeMounts:
    - name: logs-vol
      mountPath: /var/log/nginx
  volumes:
  - name: logs-vol
    emptyDir: {}
```

## Ambasador

Ambassador is a proxy for communication with external services.
E.g. provide rate limiting for max 5 calls every 15 min, rate limiting will
be provided by ambassador container.


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rate-limiter
spec:
  containers:
  - name: business-app
    image: bmuschko/nodejs-business-app:1.0.0
    ports:
    - containerPort: 8080
  - name: ambassador
    image: bmuschko/nodejs-ambassador:1.0.0
    ports:
    - containerPort: 8081
```

## Container Probes

- Health Probe - A health probe is a periodically running mini-process that asks the application for its status and takes action upon certain conditions.
- Probe Types
  - Readiness Probe - Check if the application is ready to serve.
  - Liveness probe - Once the application has started, check if it works.
  - Startup probe - legacy up, wait before starting the liveness probe.
- Verification methods
  - custom command - execute command inside the container
  - httpGet - Send HTTP GET request to an endpoint.
  - tcpSocket - Tries to open a tcp socket
### Example of readiness probe
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: readiness-pod
spec:
  containers:
  - image: bmuschko/nodejs-hello-world:1.0.0
    name: hello-world
    ports:
    - name: nodejs-port     1
      containerPort: 3000
    readinessProbe:
      httpGet:
        path: /
        port: nodejs-port   2
      initialDelaySeconds: 2
      periodSeconds: 8
```
### Example of liveness probe
- application update a file (using touch) /tmp/heatbeat.txt
Liveness
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-pod
spec:
  containers:
  - image: busybox:1.36.1
    name: app
    args:
    - /bin/sh
    - -c
    - 'while true; do touch /tmp/heartbeat.txt; sleep 5; done;'
    livenessProbe:
      exec:
        command:
        - test `find /tmp/heartbeat.txt -mmin -1`
      initialDelaySeconds: 5
      periodSeconds: 30
```


### Troubleshooting
1. Get the pods
```commandline
kubectl get pods
```
2. Get all the objects
```commandline
kubectl get all
``` 
3. Look at columns READY, STATUS, RESTARTS
4. Make sure tha t a STATUS=Running
5. Common Errors
   - ErrImagePull - image could not be pulled from registry. Check image name exists in registry.
   - CrashLoopBackOff - Application Crashed. Check command executed in a container.
   - CreateContainerConfigErr - ConfigMap not found, check config map name. 
6. Inspect events
```commandline
kubectl describe pod
```
7. Get all events
```commandline
kubectl get events
```
8. Use port forward
```commandline
kubectl port-forward nginx-595dff4799-ph4js 2500:80
```

#### Container Troubleshooting
9. libectl logs <pod name>
10. Loginto the pod
11. kubectl exec failing-pod -it -- /bash/sh
12. Inject an emphemeral containers into a pod
```commandline
kubectl alpha debug -it minimal-pod --image=busybox
```

#### Inspect Resource Metrics
1) Stored by matrix server
```commandline
minikube addons enable metrics-server
```
2) query cluste nodes and pods
```commandline
kubectl top nodes
```
```commandline
kubectl top pod frontend
```


# Resource requirements, limits and quotas
- Workload consume certain amount of resources (CPU/Mem)
- Container level - min amount of resources, Max amount of resources.
- ResourceQuota - aggegrate at the name space level
- LimitRange - specific type.
- Each container define resource request, The scheduler assure that total resource fit
- Examples:
- requests.cpu = 500ml
- requests.memopty - 64Mi
- Example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rate-limiter
spec:
  containers:
  - name: business-app
    image: bmuschko/nodejs-business-app:1.0.0
    ports:
    - containerPort: 8080
    resources:
      requests:
        memory: "256Mi"
        cpu: "1"
  - name: ambassador
    image: bmuschko/nodejs-ambassador:1.0.0
    ports:
    - containerPort: 8081
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
```
