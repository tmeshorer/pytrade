# HTTP Load balancing and ingress

Work at Layer 7 instead of Layer 4.
When solving a similar problem in non-Kubernetes situations, users often turn to the idea of “virtual hosting.” This is a mechanism to host many HTTP sites on a single IP address. Typically, the user uses a load balancer or reverse proxy to accept incoming connections on HTTP (80) and HTTPS (443) ports. That program then parses the HTTP connection and, based on the Host header and the URL path that is requested, proxies the HTTP call to some other program. In this way, that load balancer or reverse proxy directs traffic for decoding and directing incoming connections to the right “upstream” server.

 Ingress is a Kubernetes-native way to implement the “virtual hosting” pattern we just discussed
 The typical software base implementation looks something like what is depicted in Figure 8-1. The Ingress controller is a software system made up of two parts. The first is the Ingress proxy, which is exposed outside the cluster using a service of type: LoadBalancer. This proxy sends requests to “upstream” servers. The other component is the Ingress reconciler, or operator. The Ingress operator is responsible for reading and monitoring Ingress objects in the Kubernetes API and reconfiguring the Ingress proxy to route traffic as specified in the Ingress resource. There are many different Ingress implementations. In some, these two components are combined in a single container; in others, they are distinct components that are deployed separately in the Kubernetes cluster. In Figure 8-1, we introduce one example of an Ingress controller.
 Users can create and modify Ingress objects just like every other object. But, by default, there is no code running to actually act on those objects. It is up to the users (or the distribution they are using) to install and manage an outside controller. In this way, the controller is pluggable.
 
# Contour
While there are many available Ingress controllers, for the examples here, we use an Ingress controller called Contour. This is a controller built to configure the open source (and CNCF project) load balancer called Envoy. Envoy is built to be dynamically configured via an API. The Contour Ingress controller takes care of translating the Ingress objects into something that Envoy can understand.

## DNS
To make Ingress work well, you need to configure DNS entries to the external address for your load balancer. You can map multiple hostnames to a single external endpoint and the Ingress controller will direct incoming requests to the appropriate upstream service based on that hostname.


## Using ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: host-ingress
spec:
  defaultBackend:
    service:
      name: be-default
      port:
        number: 8080
  rules:
  - host: alpaca.example.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: alpaca
            port:
              number: 8080
```

```commandline
kubectl apply -f host-ingress.yaml
```
```commandline
kubectl get ingress
```
```commandline
kubectl describe ingress host-ingress
```

### Using paths

In this example, we direct everything coming into http://bandicoot.example.com to the bandicoot service, but we also send http://bandicoot.example.com/a to the alpaca serv

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: path-ingress
spec:
  rules:
  - host: bandicoot.example.com
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: bandicoot
            port:
              number: 8080
      - pathType: Prefix
        path: "/a/"
        backend:
          service:
            name: alpaca
            port:
              number: 8080
```

## Ingress controllers

- NGnix
- Emissary
- Traefik

## Will be replaced by the gateway API.
