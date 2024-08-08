# Application Observability and Maintenance

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