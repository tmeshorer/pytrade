# Kuberntes installation and configuration



#  (B) Kubernetes deployments and clusters
Creating different kinds of deployment and understanding how to work with:
- deployments api
- stateless deployment
- statefull deployments
- Pods
- Deployment
- Service
- Storage
- Ingress
- Persistance
- 
# (B) Accessing kubernetes appications and services
Work with kubernetes service to access deployments.

# (B) Scaling kubernetes applications
Scaling application up and down

# (B) Deleting applications
Understand how to delete varioud kubernetes objects.

# (B) Setting up different workloads in Kubernetes
Understand how to deploy different kind of applications, from microservices, jobs and crons

# (B) Micro Services in kubernetes
Deploying sample microservice to a cluster.

# (B) Creating Config and secret data
Dealing with configuration and secret data with clusters. Creating config maps

# (I) Working with Stateful applications
Deploying a stateful application like mongo db as stateful set.

# (I) Accessing kubernetes dashboard
Working with the kubernetes dashboard

# (I) Working with labels
Working with different labels

# (I) IngressController
Deploying an ingress controller in the cluster

# (I) Updating image registry information
Deploying applications from different registries

# (I) Pod Security Policy
Creating and updating pod security policy

# (I) Node Operation 
Working with nodes including cordoning and draining a node

# (A) Accessing logs
Working and accessing kubernetes and application logs in the cluster

# (A) Using Persistent volume and claim
Working with statefull data with persistent volume and claims

# (A) Debugging Pod Failures
Understand pod specific issues by debugging various failures in a pod.

# (A) Init Containers
Creating and using pod init container

# (A) Network Policy
Working and creating network policies for a cluster

# (A) Performance Tuning with Scheduler
Working with kubernetes scheduler including eviction policies and evicition signals




# Deployment
## Pods
```yaml
kubectl get pods
```
## Deployment
```yaml
kubectl get deployment
```
```yaml
kubectl describe deployments hello-world
```

## Replicate set
```yaml
kubectl get replicaset
```
```yaml
kubectl describe replicasets
```
## Storage

## Ingress

# Services
```yaml
kubectl get service mongo
```
### Describe
```yaml
kubectl describe services example-service
```
### Expose a deployment
```yaml
kubectl expose deployment hello-world --type=NodePort --name=example-service
```
### Forward to container
```yaml
kubectl port-forward mongo-75f59d57f4-4nd6q 28015:27017
```
### Forward to service
```yaml
kubectl port-forward service/mongo 28015:27017
```

# Scaling

# Deleting objects

# Workloads

## Job

## CronJob

# Deploy microservice
### ConfigMap

### Secret

# Working with statefull applications
# Accessing the kubernetes dashboard
```text
kubectl proxy
```
```yaml
 http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.
```

# Working with labels
# IngressController
# Updating registry information
# Pod security policy
# Node Operation
## Cardon a node
## Drain a node

# Accessing logs
# Using Presistent volume and claims
# Debug pod failures
# Init containers
# Network policy
# Perf tuning the scheulder
