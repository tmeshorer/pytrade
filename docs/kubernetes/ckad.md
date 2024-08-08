#Containers
1) k8s uses container runtime to run containers.
2) container runtime engine , run containers on host operating system.
3) container orcastror use runtme to instatiate containers 
4) container file - define how to build a container image. (Dockerfile)
5) container image is published in image registry.
```yaml
FROM azul/zulu-openjdk:21-jre                                 1
WORKDIR /app                                                  2
COPY target/java-hello-world-0.0.1.jar java-hello-world.jar   3
ENTRYPOINT ["java", "-jar", "/app/java-hello-world.jar"]      4
EXPOSE 8080 
```
6) Build the image:
```commandline
docker build -t java-hello-world:1.1.0 .
```
7) List the images:
```commandline
docker images
```
8) Run the container
```commandline
docker run -d -p 8080:8080 java-hello-world:1.1.0
```
9) List the container
```commandline
docker container ls
```
10) See container logs
```commandline
docker logs b0ee04accf07
```

11) Execute command
```commandline
docker exec -it b0ee04accf07 bash
```

12) Tag the container
```commandline
docker tag java-hello-world:1.1.0 bmuschko/java-hello-world:1.1.0
```

13) publish the container
```commandline
docker push bmuschko/java-hello-world:1.1.0
```

### Pods and namespaces
1) Pod let you run contrerinaced application
2) Pod spec container the image. Upon creating a pod, the scheduler assign the pod
   to a node. The runtime engine will download the image
```commandline
kubectl run hazelcast --image=hazelcast/hazelcast:5.1.7 \
  --port=5701 --env="DNS_DOMAIN=cluster" --labels="app=hazelcast,env=prod"
```
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
3) Create from manifest
```yaml
kubectl apply -f pod.yaml
```
4) List pods
```yaml
kubectl get pods
```
5) Pod States
 - Pending - Pod accepeted by k8s. One or more container images were created
 - Running - At least one container running
 - Succeed - All container terminated successfuly
 - Failed - At least one container failed with and error
 - Unknown - The state of the pod is unknown.

6) Show Pod details:
```commandline
kubectl describe pods hazelcast
```
7) Show pod logs:
```commandline
kubectl logs hazelcast
```

8) Execute command inside the container
```commandline
kubectl exec hazelcast -- env
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

# Working with namespaces
Namespace are used to avoid naming collision

1) List
```commandline
 kubectl get namespaces
```
2) Create
```commandline
kubectl create namespace code-red
```
3) Set current namespace
```commandline
kubectl config set-context --current --namespace=code-red
```

# Job
1) Job - one time process
2) CronJob - run on schedule
3) Upon execution of job, they stay until expliciliy deleted.
4) Create job:
```commandline
kubectl create job counter --image=nginx:1.25.1 \
  -- /bin/sh -c 'counter=0; while [ $counter -lt 3 ]; do \
  counter=$((counter+1)); echo "$counter"; sleep 3; done;'
```
5) Yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: counter
spec:
  template:   1
    spec:
      containers:
      - name: counter
        image: nginx:1.25.1
        command:
        - /bin/sh
        - -c
        - counter=0; while [ $counter -lt 3 ]; do counter=$((counter+1)); \
          echo "$counter"; sleep 3; done;
      restartPolicy: Never
```
6) Job uses a single pod. The default number of completion is 1
```commandline
 kubectl get jobs
```
7) Parallel Job:
spec.parallelisim
8) Number of retry a job attemept before successful completion
spec.backoffLimit
9) Restart Policy
spec.template.spec.restartPolicy (Always, OnFailure , Never)

### CronJob
Create new Job Poridicaly based on schedule. Based on cron expression
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: current-date
spec:
  schedule: "* * * * *"   1
  jobTemplate:            2
    spec:
      template:
        spec:
          containers:
          - name: current-date
            image: nginx:1.25.1
            args:
            - /bin/sh
            - -c
            - 'echo "Current date: $(date)"'
          restartPolicy: OnFailure
```
List cronjobs:
```commandline
 kubectl get cronjobs
```

# Volume
1) Container FS does not persist behind Pod restart.
2) Ephemeral volume exist for the life time of a pod
3) Persistent volumen preserve the data beyond the life time of a pod.
4) Mount a volume on a container
5) Volumne types
  - emptyDir - only persist for the lifespan of a Pod.
  - hostPath - File from host node FS , only for single node cluster
  - nfs - preserve data after pod restart.
  - persistentVolumeClaim
6) Epmeral Volume
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: business-app
spec:
  volumes:
  - name: logs-volume
    emptyDir: {}
  containers:
  - image: nginx:1.25.1
    name: nginx
    volumeMounts:
    - mountPath: /var/log/nginx
      name: logs-volume
```
7) Persistent Volume
- Data persist behind the lifecycle of pod/volume
- PersistentVolume - piece of storage in k8s cluster
- PersistentVolumeClaim - Request the resource of persistent volume. 
- Dynamic allocation via persistent volume class. 
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

- Read persistent volume
```yaml
kubectl get pv db-pv
```

- Persistent volumn options.
  - spec.volumeMode - FileSystem(mounts the volume into a director)
  - spec.volumeMode - Block - mount the volume as a raw block device.
- Access mode
  - ReadWriteOnce - Read/write access by a single node
  - ReadOnlyMany - Read only access by many nodes
  - ReadWriteMany - Read/Write access by many node
  - ReadWriteOncePod - R/W access mounted by a single pod.
- Reclaim policy (Specify what should happen to persistent volume when claim is deleted)
  - Retain - PersistentVolume is "released"
  - Delete - Remove the persistent volume and associate storage.

- Create PersistenVolumeClaim

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
- After creation wait for the status to be bound

```commandline
kubectl get pvc db-pvc
```

Mount the claim into a pod

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

### Storage class

A storage class is a Kubernetes primitive that defines a specific type or “class” of storage. Typical storage characteristics can be the type (e.g., fast SSD storage versus remote cloud storage or the backup policy for storage).

```commandline
kubectl get storageclass
```

Create StorageClass

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

Use storage class

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

# Multi container pods

Use cases:
- Want to initilize the pod. E.g. preconfiguration
- Want a sidecar for helper functionality. 

### Init container
Init containers provide initialization logic concerns to be run before the main application starts.

Defined in section: spec.initContainers. Cannot define probes

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
Get the log of the init container:

```commandline
kubectl logs business-app -c configurer
```

## Side car

- Used for logging, monitoring.

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

## Adapter

Run cross cutting contraints in another container. 

```yaml
  name: adapter
spec:
  containers:
  - args:
    - /bin/sh
    - -c
    - 'while true; do echo "$(date) | $(du -sh ~)" >> /var/logs/diskspace.txt; \
       sleep 5; done;'
    image: busybox:1.36.1
    name: app
    volumeMounts:
      - name: config-volume
        mountPath: /var/logs
  - image: busybox:1.36.1
    name: transformer
    args:
    - /bin/sh
    - -c
    - 'sleep 20; while true; do while read LINE; do echo "$LINE" | cut -f2 -d"|" \
       >> $(date +%Y-%m-%d-%H-%M-%S)-transformed.txt; done < \
       /var/logs/diskspace.txt; sleep 20; done;'
    volumeMounts:
    - name: config-volume
      mountPath: /var/logs
  volumes:
  - name: config-volume
    emptyDir: {}
```

## Ambasaddor Pattern

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

# Labels
1) Key-value pairs (tags on blog post)
2)
```yaml
tier:backend
env:dev
app:crawler
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: labeled-pod
  labels:
    env: dev
    tier: backend
spec:
  containers:
  - image: nginx:1.25.1
    name: nginx
```
3) Check pod labels:
```yaml
 kubectl describe pod labeled-pod
```

4) Modify the labels:
```commandline
kubectl label pod labeled-pod region=us --overwrite
```

5) Query using labels
```commandline
kubectl get pods -l 'team in (shiny, legacy)' --show-labels
```

6) Used by kubernetes object

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-network-policy
spec:
  podSelector:
    matchLabels:
      tier: frontend
```

Recommended Labels

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/version: "1.25.1"
    app.kubernetes.io/component: server
spec:
  containers:
  - name: nginx
    image: nginx:1.25.1
```

Annotation
-----
Describe descriptive metadata.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: annotated-pod
  annotations:
    commit: 866a8dc
    author: 'Benjamin Muschko'
    branch: 'bm/bugfix'
spec:
  containers:
  - image: nginx:1.25.1
    name: nginx
```

Set annotation:

```commandline
kubectl annotate pod annotated-pod oncall='800-555-1212'
```

ReplicaSet control multiple identical pods.
Deployment manage ReplicaSet.

Create Deployment

```commandline
kubectl create deployment app-cache --image=memcached:1.6.8 --replicas=4
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-cache
  labels:
    app: app-cache
spec:
  replicas: 4
  selector:
    matchLabels:
      app: app-cache
  template:
    metadata:
      labels:
        app: app-cache
    spec:
      containers:
      - name: memcached
        image: memcached:1.6.8
```
Assign matchLabels equals labels. Deplyment automatically create replicaset.

List Deployment

```commandline
kubectl get deployments
```

Kubernetes keeps track of the changes you make to a Deployment over time in the rollout history. Every change is represented by a revision. When changing the Pod template of a Deployment—for example, by updating the image—the Deployment triggers the creation of a new ReplicaSet. The Deployment will gradually migrate the Pods from the old ReplicaSet to the new one. You can check the rollout history by running the following command. You will see two revisions listed:
See the rollout status
```commandline
$ kubectl rollout status deployment app-cache
```
rollout history
```commandline
kubectl rollout history deployment app-cache
```
Show detailed rolloput history
```commandline
kubectl rollout history deployments app-cache --revision=2
```
Show change cause - add an annotation 

```commandline
kubectl annotate deployment app-cache kubernetes.io/change-cause=\
"Image updated to 1.6.10"
```
Rolling back
kubectl rollout undo deployment app-cache --to-revision=1

### Scaling workload
Manual scaling
```commandline
kubectl scale deployment app-cache --replicas=6
```
### Autoscaling
Using HPA - horizontal pod autoscaler
- can scale on target value/avarge value / avarage utilization
- CPU or memory
- Must have metrics server installed.
- set via the command line
```commandline
kubectl autoscale deployment app-cache --cpu-percent=80 --min=3 --max=5
```
- create an HPA
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-cache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-cache
  minReplicas: 3
  maxReplicas: 5
  metrics:
  - resource:
      name: cpu
      target:
        averageUtilization: 80
        type: Utilization
    type: Resource
```
- List hpa
```commandline
kubectl get hpa
```
- Show hpa details
```commandline
kubectl describe hpa app-cache
```
- Define multiple scaling metrics
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-cache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-cache
  minReplicas: 3
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
  - type: Resource
    resource:
      name: memory
      target:
        type: AverageValue
        averageValue: 500Mi
```