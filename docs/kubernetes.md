1. Container Orchestrator 
2. Orchestrator
   -  deployment - deploy one or more replicas.
   -  update strategies
   -  scheduling
   -  rollback 
   -  auto scaling (vertical auto scaler)
   -  auto healing: monitor app health. 
   -  secret management. 
   -  load balancing - run mutiple replicate of your apps, need way to distribute replicas.
   -  service communication : authentication / authrization / encryption / error handling 
3. Load balancer - distribute load across multiple servers or apps.
   - round robin / hash based / least response time. 
   - Apache , nginx, haproxy. 
- VM Orchestrator - AWS auto scaling group. Scale the number of servers up or down. 
  - create VM image / deploy VM image / scale VM image.
  - AWS open scaling group - auto scaling / auto healing
  - GCP managed instance group  - cluster managements. 
  - lanch template
  - security groups
  - VPC - virtual private cloud . has its own virtual network , IP address space. 
  - AWS load balancer or GCP load balancer. 
  - AWS - application load balancer.
- Container orchestrator
  - create container image.
  - deploy container image
  - automatically scale the servers up or down  
- Docker
  - Docker image - self contains snapshot of the OS, software, files
  - Docker hub - docker registry of shared docker images. 
  - Docker file - template that define how to build docker image
  - Docker engine manages process supervision, etc. 
  - ```dockerfile
    FROM node:21.7 1
    
    WORKDIR /home/node/app 2
    
    COPY app.js . 3
    
    EXPOSE 8080 4
    
    USER node 5
    
    CMD ["node", "app.js"] 6
    ```
  - build docker image
  - run docker image
    ```commandline
    docker run -p 8080:8080 --init sample-app:v1
    ```
  - Expose docker port 8080 inside the container to host port 8080.
  
## Kubernetes 
   
container orchestration tool. platform for managing containers on your servers.
- auto healing / auto scaling / load balancing 
- control plane - managing the kuberntes cluster , store the state of the cluster, 
  run the api server.
- create kubernetes object. record of intent. kubernetes recocile 
- kubernetes objects - kubectl apply.
  - pod - group of containers. ports, envvars
  - replica set
  - deployment - selector - what to target
    ```yaml 
    apiVersion: apps/v1
    kind: Deployment                  1
    metadata:                         2
      name: sample-app-deployment
    spec:
      replicas: 3                     3
      template:                       4
        metadata:                     5
          labels:
            app: sample-app-pods
        spec:
          containers:                 6
            - name: sample-app        7
              image: sample-app:v1    8
              ports:
                - containerPort: 8080 9
              env:                    10
                - name: NODE_ENV
                  value: production
      selector:                       11
        matchLabels:
          app: sample-app-pods   
    
    
    ``` 
    - kubernetes service - expose an app running on kubernetes.
      ```yaml
      apiVersion: v1
      kind: Service                    1
      metadata:                        2
        name: sample-app-loadbalancer
      spec:
        type: LoadBalancer             3
        selector:
          app: sample-app-pods         4
        ports:
          - protocol: TCP
            port: 80                   5
            targetPort: 8080           
        ``` 
      - AWS - get AWS elb. 
      - Receive request in port 80 forward to port 8080. 

## Kubernetes concepts
- control loop
- sevices
- workload
- storage.

## Kubernetes objects
1. Nodes
2. Pods - how , when and where things run. just pod limit you if host die.
3. ReplicateSet - right number of replicas are running all the times.
4. Namespaces
4. Deployment - Ensure that the right number of pods with the right image are running.
5. Service - provide stable identity / load balancing / service discovery.
6. DeamonSet
7. Events
8. Logs
9. ServiceAccount
10. ReplicaSet
11. Roles
12. Secrets
13. ConfigMap
14. Ingress
15. EmphmeralVolume - life cycle tied to a pod. E.g. for caching
15. PersistantVolume - back 
16. PersistentVolumeClaim
17. HorizentalPodAutoscaler - scale the nodes based on CPU. 
