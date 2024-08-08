#Service Discovery
- While the dynamic nature of Kubernetes makes it easy to run a lot of things, it creates problems when it comes to finding those things. Most of the traditional network infrastructure wasn’t built for the level of dynamism that Kubernetes presents.
- Service-discovery tools help solve the problem of finding which processes are listening at which addresses for which services. 
- The Domain Name System (DNS) is the traditional system of service discovery on the internet.
- Unfortunately, many systems (for example, Java, by default) look up a name in DNS directly and never re-resolve it. This can lead to clients caching stale mappings and talking to the wrong IP

# Service Object
- Expose
  ```commandline
  kubectl expose deployment alpaca-prod
  ```
  Furthermore, that service is assigned a new type of virtual IP called a cluster IP. This is a special IP address the system will load balance across all of the Pods that are identified by the selector.
- Use port forward
  ```commandline
  kubectl port-forward $ALPACA_POD 48858:8080
  ```
## DNS Service
- Because the cluster IP is virtual, it is stable, and it is appropriate to give it a DNS address
- Within a namespace, it is as easy as just using the service name to connect to one of the Pods identified by a service.
- Kubernetes provides a DNS service exposed to Pods running in the cluster. This Kubernetes DNS service was installed as a system component when the cluster was first created. 
- Full DNS:
  ```commandline
  alpaca-prod.default.svc.cluster.local.
  ```
## Readiness check
```yaml
spec:
  ...
  template:
    ...
    spec:
      containers:
        ...
        name: alpaca-prod
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          periodSeconds: 2
          initialDelaySeconds: 0
          failureThreshold: 3
          successThreshold: 1

```
## NodePort

The most portable way to do this is to use a feature called NodePorts, which enhance a service even further. In addition to a cluster IP, the system picks a port (or the user can specify one), and every node in the cluster then forwards traffic to that port to the service.

## External load balancer
If you have a cluster that is configured to integrate with external load balancers, you can use the LoadBalancer type. This builds on the NodePort type by additionally configuring the cloud to create a new load balancer and direct it at nodes in your cluster. Most cloud-based Kubernetes clusters offer load balancer integration, and there are a number of projects that implement load balancer integration for common physical load balancers as well, although these may require more manual integration with your cluster.


## End points

Some applications (and the system itself) want to be able to use services without using a cluster IP. This is done with another type of object called an Endpoints object. For every Service object, Kubernetes creates a buddy Endpoints object that contains the IP addresses for that service:

```commandline
kubectl describe endpoints alpaca-prod
```
## KubeProxy

In Figure 7-1, the kube-proxy watches for new services in the cluster via the API server. It then programs a set of iptables rules in the kernel of that host to rewrite the destinations of packets so they are directed at one of the endpoints for that service. If the set of endpoints for a service changes (due to Pods coming and going or due to a failed readiness check), the set of iptables rules is rewritten.

The cluster IP itself is usually assigned by the API server as the service is created. However, when creating the service, the user can specify a specific cluster IP. Once set, the cluster IP cannot be modified without deleting and re-creating the Service object.

## Add external service

1. Create a service with no selector
2. Add Endpoint object.



